import gradio as gr
import tools.customer_common_funcs as ccf
import os


# 切分多段操作
def split_operation(video_files, video, input_number, input_number_point, overlap_input_number):
    # 获取分片视频输出临时路径
    template_filepath = os.getenv("SPLIT_VIDEO_TEMP_FOLDER")

    # 删除临时文件夹下的内容
    ccf.delete_folder_contents(template_filepath)

    # 切割视频文件
    split_audio_paths = ccf.split_video(video_file=video, output_dir=template_filepath, split_length_seconds=input_number, overlap_seconds=overlap_input_number)

    return split_audio_paths,template_filepath


# 切分两段
def split4two_operation(video_files, video, input_number, input_number_point, overlap_input_number):
    # 获取分片视频输出临时路径
    template_filepath = os.getenv("SPLIT_VIDEO_TEMP_FOLDER")

    # 删除临时文件夹下的内容
    ccf.delete_folder_contents(template_filepath)

    # 切割视频文件
    split_audio_paths = ccf.split_video_two(
        video_file=video, output_dir=template_filepath,point_time_seconds=input_number_point)

    return split_audio_paths, template_filepath


# 字幕提取
def extract_subtitle_operation(video_files, video, input_number, input_number_point, overlap_input_number):
    # 获取分片视频输出临时路径
    template_filepath = os.getenv("SUBTITLE_TEMP_FOLDER")

    # 删除临时文件夹下的内容
    ccf.delete_folder_contents(template_filepath)

    # 切割视频文件
    extract_subtitles_paths = ccf.extract_subtitles(
        video_files, template_filepath)

    return extract_subtitles_paths, template_filepath


def submit_result(op, input_files, video, input_number, input_number_point, overlap_input_number):

    # 定义函数字典
    dict_operations = {
        "字幕提取": extract_subtitle_operation,
        "切分多段": split_operation,
        "切分两段": split4two_operation
    }

    video_paths, template_filepath = dict_operations[op](
        input_files, video, input_number, input_number_point, overlap_input_number)

    # 获取基础路径 
    current_file_path = os.path.abspath(__file__) 
    directory, _  = os.path.split(current_file_path)
    bashpath, _ = os.path.split(directory)

    # 输出视频文件所在全路径
    audio_fullpath = os.path.join(bashpath, template_filepath)
    
    return video_paths, audio_fullpath
    

def clear_result():
    return gr.Files(), gr.Video(), gr.Numpy(value=10), gr.Numpy(value=10), gr.Numpy(value=1)

def update_select(op):

    if (op == "字幕提取"):
        return gr.Files(visible=True), gr.Video(visible=False), gr.Number(visible=False), gr.Number(visible=False), gr.Number(visible=False)
    elif (op == "切分多段"):
        return gr.Files(visible=False), gr.Video(visible=True), gr.Number(visible=True), gr.Number(visible=False), gr.Number(visible=True)
    else:    
        return gr.Files(visible=False), gr.Video(visible=True), gr.Number(visible=False), gr.Number(visible=True), gr.Number(visible=False)
    

def func():
    with gr.Row():
        with gr.Column():
            op_radio = gr.Radio(["切分多段", "切分两段", "字幕提取"],
                                label="操作类型", info="请选择操作类型:", value="切分多段")
            input_files = gr.Files(label="文件", type='filepath',
                                   file_count="directory", visible=False)
            input_video = gr.Video(label="输入视频",sources=["upload"])
            input_number = gr.Number(label="分割片段长度[单位:秒]", value=10 ,minimum=1)
            overlap_input_number = gr.Number(label="重叠长度[单位:秒]", value=1 ,minimum=0)
            input_number_point = gr.Number(
                label="切割点[单位:秒]", value=10, minimum=1, visible=False)
            with gr.Row():
                with gr.Column():
                    clear_btn = gr.Button(value="清空")
                with gr.Column():
                    submit_btn = gr.Button("提交", variant="primary")
        with gr.Column():
            output_audio = gr.File(label="结果输出明细")
            ouput_text = gr.Textbox(label="结果路径")

    # radio 操作修改事件
    op_radio.change(fn=update_select, inputs=[op_radio], outputs=[input_files,input_video,
                    input_number, input_number_point, overlap_input_number])

    # 设置清空点击事件
    clear_btn.click(fn=clear_result, inputs=[], outputs=[
                    input_files, input_video, input_number, input_number_point, overlap_input_number])

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[op_radio, input_files, input_video, input_number,input_number_point,overlap_input_number],
                     outputs=[output_audio, ouput_text])
