import gradio as gr
import tools.customer_common_funcs as ccf
import os


# 切分操作
def split_operation(files, audio, input_number):
    # 获取分片音频输出临时路径
    template_filepath = os.getenv("SPLIT_AUDIO_TEMP_FOLDER")

    # 删除临时文件夹下的内容
    ccf.delete_folder_contents(template_filepath)

    # 切割音频文件
    split_audio_paths = ccf.split_audio(
        audio_file=audio, output_dir=template_filepath, split_length_seconds=input_number)

    return split_audio_paths,template_filepath


# 合并操作
def merge_operation(files, audio, input_number):
    # 获取合并音频输出临时路径
    template_filepath = os.getenv("MERGE_AUDIO_TEMP_FOLDER")

    # 删除临时文件夹下的内容
    ccf.delete_folder_contents(template_filepath)

    # 合并音频文件
    merge_audio_paths = ccf.merge_audio(
        audio_files=files, output_dir=template_filepath)

    return merge_audio_paths,template_filepath


def submit_result(op,files,audio,input_number):

    # 定义函数字典
    dict_operations = {
        "切分": split_operation,
        "合并": merge_operation
    }

    audio_paths, template_filepath = dict_operations[op](
        files, audio, input_number)

    # 获取基础路径 
    current_file_path = os.path.abspath(__file__) 
    directory, _  = os.path.split(current_file_path)
    bashpath, _ = os.path.split(directory)

    # 输出音频文件所在全路径
    audio_fullpath = os.path.join(bashpath, template_filepath)
    
    return audio_paths, audio_fullpath
    

def clear_result():
    return gr.Files(),gr.Audio(),gr.Numpy(value=60),gr.File()


def update_select(op):

    if(op == "切分"):
        return gr.Files(visible=False,value=[]), gr.Audio(visible=True), gr.Number(visible=True)
    else:
        return gr.Files(visible=True,value=[]), gr.Audio(visible=False), gr.Number(visible=False)
    

def func():
    with gr.Row():
        with gr.Column():
            op_radio = gr.Radio(["切分", "合并"],
                                label="操作类型", info="请选择操作类型:", value="切分")
            input_files = gr.Files(label="文件", type='filepath',
                                   file_count="directory", visible=False)
            input_audio = gr.Audio(label="输入音频",sources=["upload"], type='filepath')
            input_number = gr.Number(label="分割片段长度[单位:秒]", value=60 ,minimum=15)
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_audio = gr.File(label="输出音频")
            ouput_text = gr.Textbox(label="输出音频路径")

    # radio 操作修改事件
    op_radio.change(fn=update_select, inputs=[op_radio], outputs=[input_files, input_audio, input_number])                

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    input_files,input_audio, input_number, output_audio])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[op_radio, input_files, input_audio, input_number],
                     outputs=[output_audio, ouput_text])
