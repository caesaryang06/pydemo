import os 


def main(directory,writeFile):
    video_files = []
    for root,dirs,files in os.walk(directory):
        for filename in files:
            video_files.append(f"{root}{filename}")


   # 写入文件        
    with open(writeFile, "w") as f:
        f.writelines(video_files)
          







if __name__ == "__main__":
    directory = "C:/Users/yangxinmin/Desktop/workspace/唱歌源视频/竖屏/"
    writeFile = "data/comfyui_video_info.txt"
    main(directory=directory, writeFile=writeFile)
