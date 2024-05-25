import gradio as gr


def submit_result(图片, name, is_morning, temperature, 音乐):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9

    return {'cat': 0.3, 'dog': 0.7}, greeting, round(celsius, 2), gr.make_waveform(音乐)


def clear_result():
    return "", ""


def func():
    with gr.Row():
        with gr.Column():
            input_image = gr.Image()
            input_text = gr.Textbox()
            input_checbox = gr.CheckboxGroup(["复选框1", "复选框2", "复选框3"])
            input_slider = gr.Slider(0, 100, 50, step=1, label="滑块")
            input_audio = gr.Audio()
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_label = gr.Label()
            output_text = gr.Textbox()
            output_number = gr.Number(label="数字")
            output_video = gr.Video(label="视频")

            output_text2 = gr.Textbox(label="密码加密后的结果")

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    input_text, output_text])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[input_image, input_text, input_checbox, input_slider, input_audio],
                      outputs=[output_label, output_text, output_number,output_video])