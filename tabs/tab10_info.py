import gradio as gr
from tools import custom_codec as cc
import pandas as pd 
import os 

## 定义一个函数  用于新增邮箱  包含两个参数  邮箱地址和邮箱密码
def add_email(email, password):
    email_data_file = os.getenv("EMAIL_MANAGER_DATA")

    df = pd.read_excel(email_data_file)
    df.loc[len(df.index)] = [email, password]

    # 对数据去重
    df.drop_duplicates(subset=['邮箱地址'], keep='first', inplace=True)

    # 保存数据
    df.to_excel(email_data_file, index=False)


    return df


## 定义一个函数  用于删除邮箱  包含两个参数  邮箱地址和邮箱密码
def delete_email(email, password):
    email_data_file = os.getenv("EMAIL_MANAGER_DATA")
    df = pd.read_excel(email_data_file)
    df.drop(df[df['邮箱地址'] == email].index, inplace=True)

    # 保存数据
    df.to_excel(email_data_file, index=False)

    return df


def submit_result(op, input_email, input_passwd):
    """
    新增或者删除邮箱
    输入: 操作类型,邮箱地址，邮箱密码
    输出: 输出文本
    """

    # 定义函数字典
    dict = {
        "新增": add_email,
        "删除": delete_email
    }

    func_name = dict[op]

    if func_name:
        return func_name(input_email, input_passwd)
    else:
        return "无效的操作类型"


def clear_result():
    return "", ""


def func():
    with gr.Row():
        with gr.Column():
            op_radio = gr.Radio(["新增", "删除"],
                                label="操作类型", info="请选择操作类型:", value="新增")
            input_email = gr.Textbox(label="邮箱地址")
            input_passwd = gr.Textbox(label="邮箱密码")
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_numpy = gr.Numpy(col_count=2, headers=["邮箱地址", "邮箱密码"])

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    input_email, input_passwd])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[
                     op_radio, input_email, input_passwd], outputs=[output_numpy])
