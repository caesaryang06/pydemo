import gradio as gr
from tools import custom_codec as cc
import pandas as pd 
import os 

from IPython.display import Audio
from tabs.ChatTTS import ChatTTS
import torch
import torchaudio
torch._dynamo.config.cache_size_limit = 64
torch._dynamo.config.suppress_errors = True
torch.set_float32_matmul_precision('high')



# 定义函数  文本转语音
def text_to_speech(text):

    # 输出音频临时路径
    chattts_temp_folder = os.getenv("CHATTTS_TEMP_FOLDER")

    # 加载模型
    chat = ChatTTS.Chat()
    chat.load_models(compile=True)  # Set to True for better performance

    # 文本内容 
    texts = [
        text,
    ]

    # Perform inference and play the generated audio
    wavs = chat.infer(texts)
    Audio(wavs[0], rate=24_000, autoplay=True)

    # Save the generated audio
    outpath_audio = chattts_temp_folder  + "/output.wav"
    torchaudio.save(outpath_audio, torch.from_numpy(wavs[0]), 24000)

    return outpath_audio



def submit_result(text):
    """
    文本转语音
    输入: 文本
    输出: 输出文本和音频
    """
    output_audio = text_to_speech(text)
    return text, output_audio


def func():
    with gr.Row():
        input_area = gr.TextArea(label="文本内容")
        submit_btn = gr.Button("生成", variant="primary")
        output_area = gr.TextArea(label="输出文本")
        output_audio = gr.Audio(label="音频输出", type='filepath')

    # 设置提交点击事件
    submit_btn.click(fn=submit_result, inputs=[input_area], outputs=[output_area, output_audio])
