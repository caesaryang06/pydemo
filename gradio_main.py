import gradio as gr
from tabs import tab1_info, tab2_info, tab3_info, tab4_info, tab5_info, tab6_info, tab7_info, tab8_info, demo_info

# 加载 .env 文件
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())



# 登录验证函数
def login(username, password):
    return username == "admin" and password == "admin"



if __name__ == "__main__":
    with gr.Blocks() as app:
        with gr.Tabs():
            with gr.Tab("生成随机密码"):
                tab1_info.func()
            with gr.Tab("密码加解密"):
                tab2_info.func()
            with gr.Tab("脚本执行"):
                tab3_info.func()
            with gr.Tab("模版维护"):
                tab4_info.func()
            with gr.Tab("音频处理"):
                tab5_info.func()  
            with gr.Tab("函数查看器"):
                tab6_info.func()
            with gr.Tab("视频处理"):
                tab7_info.func()
            with gr.Tab("comfyui流执行"):
                tab8_info.func()
            with gr.Tab("测试"):
                demo_info.func()
    app.launch(share=False, auth=login)
    
