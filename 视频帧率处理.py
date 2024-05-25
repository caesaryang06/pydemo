from moviepy.editor import VideoFileClip
import shutil
from moviepy.editor import VideoFileClip
import os


# 获取视频帧率
def get_frame_rate(video_path):
    # 加载视频文件
    clip = VideoFileClip(video_path)
    # 获取帧率
    frame_rate = clip.fps
    # 关闭视频文件，释放资源
    clip.close()
    return frame_rate


# 拷贝视频
def copy_video(source_path, destination_path):
    # 复制视频文件
    shutil.copy(source_path, destination_path)


# 拷贝视频并强制帧率30
def reduce_frame_rate(input_video_path, output_video_path):
    # 加载视频文件
    clip = VideoFileClip(input_video_path)
    # 设置新的帧率
    new_clip = clip.set_fps(30)
    # 输出新的视频文件
    new_clip.write_videofile(output_video_path, codec='libx264')






def main(input_dir,out_dir):
    number = 1
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            numberStr = str(number).zfill(4)
            with open(f"{out_dir}/{numberStr}.txt", 'a', encoding='utf-8') as f:
                f.write(file.replace(".mp4", ""))
            newVideoFile = f"{out_dir}/{numberStr}.mp4"
            frame_rate = get_frame_rate(f"{root}/{file}")
            if frame_rate > 30:
                # 强制帧率为30
                reduce_frame_rate(f"{root}/{file}",newVideoFile)
            elif frame_rate == 30:
                # 拷贝视频
                copy_video(f"{root}/{file}",newVideoFile)
                print("帧率正常")       
            number += 1


                





if __name__ == '__main__':
    input_dir = "C:/Users/yangxinmin/Desktop/workspace/抖音视频/隋小懿"
    out_dir = "C:/Users/yangxinmin/Desktop/workspace/唱歌源视频/竖屏"
    main(input_dir=input_dir,out_dir=out_dir)

