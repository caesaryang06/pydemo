import gradio as gr



def submit_result():

    return "测试"


def clear_result():
    return ""


def update_options():
    options = ['FFIU', 'IGEB', 'VCIT', 'FCOR', 'SKOR', 'KORP', 'LQDI']
    return gr.Dropdown(choices=options, interactive=True)

def tab2_func():
    with gr.Row():
        with gr.Column():
            input_dropdown = gr.Dropdown(
                label="选择一个模版名", choices=["aa","bb"], interactive=True)
            reflash_btn = gr.Button("刷新") 
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_text = gr.Textbox(label="输出内容")

    # 刷新按钮点击事件
    reflash_btn.click(fn=update_options, inputs=[], outputs=[input_dropdown])


    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    output_text])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[], 
                      outputs=[output_text])

with gr.Blocks() as app:
    with gr.Tabs():
        with gr.Tab("模版维护"):
            tab2_func()


app.launch()
