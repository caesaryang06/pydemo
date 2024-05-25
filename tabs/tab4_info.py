import gradio as gr
import pandas as pd
import os


# 定义添加操作类型处理函数
def add_operation(df, temp_name, temp_content):
    # 要添加或更新的记录信息
    new_record = {'模版名': temp_name, '模版内容': temp_content}

    # 检查记录是否已存在
    if new_record['模版名'] in df['模版名'].values:
        # 如果记录已存在，使用.loc或.at来更新它
        df.loc[df['模版名'] == new_record['模版名'], '模版内容'] = new_record['模版内容']
    else:
        # 如果记录不存在，使用.append来添加它
        add_df = pd.DataFrame({'模版名': [temp_name], '模版内容': [temp_content]})
        df = pd.concat([df, add_df], ignore_index=True)

    return df


# 定义删除操作类型处理函数
def delete_operation(df, temp_name, temp_content):

    # 删除指定模版名对应的记录行
    df.drop(df[df['模版名'] == temp_name].index, inplace=True)

    return df


def submit_result(op, temp_name, temp_content):
    # 读取Excel中记录的数据
    template_filepath = os.getenv("TEMPLATE_FILEPATH")
    df = pd.read_excel(template_filepath, engine='openpyxl')

    # 定义函数字典
    dict_operations = {
        "添加": add_operation,
        "删除": delete_operation
    }
    if temp_name:

        # 根据操作类型进行不同处理
        df = dict_operations[op](df, temp_name, temp_content)

        # 保存到Excel
        df.to_excel(template_filepath, index=False, engine='openpyxl')

    return df


def clear_result():
    return "", ""


def func():
    with gr.Row():
        with gr.Column():
            op_radio = gr.Radio(["添加", "删除"],
                                label="操作类型", info="请选择操作类型:", value="添加")
            temp_name_input = gr.Textbox(label="模版名")
            temp_content_input = gr.TextArea(label="模版内容")
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_numpy = gr.Numpy(col_count=2, headers=["模版名", "模版内容"])

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    temp_name_input, temp_content_input])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[op_radio, temp_name_input,temp_content_input], outputs=[output_numpy])