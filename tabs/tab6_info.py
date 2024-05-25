import gradio as gr
from tools import customer_common_funcs as ccf




# 字典
dict = {

   "函数处理器一":ccf.string_processor_01,

}


# 查看操作
def view_operation(process_dropdown, input_text):
    into =  dict[process_dropdown].__doc__
    return [into]

# 测试操作
def test_operation(process_dropdown, input_text):
     
    return dict[process_dropdown](input_text)

# 提交事件
def submit_result(op, process_dropdown, input_text):

    # 定义函数字典
    dict_operations = {
        "查看": view_operation,
        "测试": test_operation
    }

    list = dict_operations[op](process_dropdown, input_text)

    return "\n".join(list)

#清空事件
def clear_result():
    return "", ""

# 修改操作类型事件
def change_result(op):
    if op == "查看":
        return gr.TextArea(visible=False), ""
    else:
        return gr.TextArea(visible=True), ""

def func():
    with gr.Row():
        with gr.Column():
            op_radio = gr.Radio(choices=["查看", "测试"], label="操作类型")
            process_dropdown = gr.Dropdown(
                label="选择一个函数处理器", choices=list(dict.keys()))
            input_text = gr.TextArea(label="输入文本")
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
            output_area = gr.TextArea(label="结果")


    # radio 修改事件
    op_radio.change(change_result, inputs=[op_radio], outputs=[input_text, output_area])                

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    input_text,output_area])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[op_radio,process_dropdown,input_text],
                     outputs=[output_area])
