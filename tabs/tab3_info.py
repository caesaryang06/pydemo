import gradio as gr
import pandas as pd
import re
import os


def get_choice():
    # 获取模版文件中的所有模版名
    template_filepath = os.getenv("TEMPLATE_FILEPATH")
    df = pd.read_excel(template_filepath, engine='openpyxl')
    return df['模版名'].values.tolist()


def update_input(selected_option):
    # 根据选择的下拉选项更新输入框内容
    template_filepath = os.getenv("TEMPLATE_FILEPATH")
    df = pd.read_excel(template_filepath, engine='openpyxl')
    value = df[df['模版名'] == selected_option]['模版内容'].values[0]
    
    return value


def refresh_result():
    return gr.Dropdown(choices=get_choice(), interactive=True)


def submit_result(temp_content, input):
    """
    根据模版对文本进行处理
    输入: 模版内容,输入文本
    输出: 基于模版内容处理后的文本
    样例: 模版内容: 我要{}成为{}的存在; 输入文本为: 小白@@@@伟人; 输出: 我要小白成为伟人的存在  
    """

    list = []

    lines = re.split(r'\r?\n', input)

    for line in lines:
        values = line.split("@@@@")
        list.append(temp_content.format(*values))

    return "\n".join(list)


def clear_result():
    return "", ""


def func():
    with gr.Row():
        with gr.Column():
            with gr.Row():
                with gr.Column(scale=3):
                    dropdown = gr.Dropdown(
                        label="选择一个模版名", choices=get_choice(), interactive=True)
                with gr.Column(scale=1):
                    refresh_btn = gr.Button(
                        value="刷新", icon="icon/refresh.icon")
            input_text = gr.Textbox(label="模版内容", interactive=False)
            input_area = gr.TextArea(
                label="输入文本", info="样例: xx小白@@@@伟人xxxxxxxxxxxxxx")
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_text = gr.TextArea(label="输出框")

    # 设置下拉选项修改事件
    dropdown.change(fn=update_input, inputs=dropdown,
                    outputs=input_text)
    
    # 刷新按钮点击事件
    refresh_btn.click(fn=refresh_result, inputs=[],outputs=[dropdown])

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[],
                    outputs=[input_area, output_text])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result,
                     inputs=[input_text, input_area], outputs=output_text,)
