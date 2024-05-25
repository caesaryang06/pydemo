import json
import requests
import tools.customer_common_funcs as common_funcs
from tools.common_log import setup_logger
import os 


#######################################基础配置#########################################################
URL = "{}/prompt"
WORKFLOW_BASE_PATH = "D:/vscode-pro/py_demo/workflow"

############################################工具########################################################
WORKFLOW_TOOLS_COMBINEVIDEO = f"{WORKFLOW_BASE_PATH}/工具/视频合并_online.json"

#########################################动画01###########################################################
WORKFLOW_JSONPATH_11 = f"{WORKFLOW_BASE_PATH}/动画/1_视频预处理.json"
WORKFLOW_JSONPATH_12 = f"{WORKFLOW_BASE_PATH}/动画/2_animation_raw.json"
WORKFLOW_JSONPATH_13 = f"{WORKFLOW_BASE_PATH}/动画/3_animation_refiner.json"
WORKFLOW_JSONPATH_14 = f"{WORKFLOW_BASE_PATH}/动画/4_animation_facefix.json"
#######################################################################################################
######################################### 动画02###########################################################
WORKFLOW_JSONPATH_21 = f"{WORKFLOW_BASE_PATH}/动画2/01_源视频处理.json"
WORKFLOW_JSONPATH_22 = f"{WORKFLOW_BASE_PATH}/动画2/02_视频转绘.json"
#######################################################################################################

######################################### 动画03###########################################################
WORKFLOW_JSONPATH_31 = f"{WORKFLOW_BASE_PATH}/动画3/视频转动漫.json"
#######################################################################################################



# 根据视频获取处理批次
def get_batchs(batch_range,video_path):
    result = []
    skip_frame = 0
    total_frame = min(common_funcs.get_frame_count(video_path),480)
    while skip_frame < total_frame:
        result.append((skip_frame,batch_range))
        skip_frame += batch_range

    return result

# 动画流执行
def queue_prompt(prompt,url):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    response = requests.post(url, data=data)

# 视频合并


def exec_workflow_combinevideo(base_path, images, video_filename, url, frame_rate=24):
    json_file = WORKFLOW_TOOLS_COMBINEVIDEO
    with open(json_file, 'r', encoding='utf-8') as jsonFile:
        prompt = json.load(jsonFile)

    # 指定基本路径
    prompt["158"]["inputs"]["string"] = base_path
    # 指定帧率
    prompt["53"]["inputs"]["Number"] = frame_rate

    # 指定images1路径
    prompt["159"]["inputs"]["string"] = images
    # 指定视频前缀
    prompt["190"]["inputs"]["string"] = "alan_" + video_filename 


    # 调用json文件
    queue_prompt(prompt,url)       


# 视频转动漫  1
def exec_workflow_video2video_01(video_path,base_path,step_dict,url):
    # 执行第一个工作流
    if "1" in step_dict.keys():
        json_file = WORKFLOW_JSONPATH_11
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)

        # 获取帧数
        total_frame = common_funcs.get_frame_count(video_path)
        # 跳过帧数
        skip_frame = 0
        lap_counter = 0
        while skip_frame < total_frame:

            # 指定视频路径  video
            prompt["584"]["inputs"]["string"] = video_path
            # 指定基本路径
            prompt["109"]["inputs"]["string"] = base_path
            # Batch Range
            prompt["583"]["inputs"]["seed"] = 120
            # Lap Counter
            prompt["585"]["inputs"]["seed"] = lap_counter

            lap_counter += 1
            skip_frame = lap_counter * 120

            # 调用json文件
            queue_prompt(prompt,url)

    if "2" in step_dict.keys():
        # 执行第二个工作流
        json_file = WORKFLOW_JSONPATH_12
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)
  
        for skip_frame, batch_range in get_batchs(120,    video_path):
            # 指定基本路径
            prompt["455"]["inputs"]["string"] = base_path
            # 修改输入参数 Skip Frame
            prompt["172"]["inputs"]["start_index"] = skip_frame
            # Batch Range
            prompt["172"]["inputs"]["image_load_cap"] = batch_range

            # 修改输入参数 Skip Frame
            prompt["174"]["inputs"]["start_index"] = skip_frame
            # Batch Range
            prompt["174"]["inputs"]["image_load_cap"] = batch_range

            # Batch Size
            prompt["151"]["inputs"]["batch_size"] = batch_range

            # 调用json文件
            queue_prompt(prompt,url)

    if "3" in step_dict.keys():
        # 执行第三个工作流
        json_file = WORKFLOW_JSONPATH_13
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)

        for skip_frame, batch_range in get_batchs(120,    video_path):
            # 指定基本路径
            prompt["169"]["inputs"]["string"] = base_path
            # 修改输入参数 Skip Frame  ControlNet 1
            prompt["17"]["inputs"]["start_index"] = skip_frame
            # 修改输入参数 Skip Frame  ControlNet 2
            prompt["20"]["inputs"]["start_index"] = skip_frame
            # 修改输入参数 Skip Frame  Raw Images
            prompt["21"]["inputs"]["start_index"] = skip_frame

            # Batch Range
            prompt["153"]["inputs"]["int"] = batch_range

            # 调用json文件
            queue_prompt(prompt,url)

    if "4" in step_dict.keys():
        # 执行第四个工作流
        json_file = WORKFLOW_JSONPATH_14
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)

        for skip_frame, batch_range in get_batchs(120,    video_path):
            # 指定基本路径
            prompt["92"]["inputs"]["string"] = base_path
            # 修改输入参数 Skip Frame  Input Refined Images
            prompt["21"]["inputs"]["start_index"] = skip_frame
            # 修改输入参数 Skip Frame  Input Refined Images
            prompt["21"]["inputs"]["image_load_cap"] = batch_range

            # 调用json文件
            queue_prompt(prompt,url)


# 视频转动漫  2
def exec_workflow_video2video_02(win_video_path, centos_video_path, base_path, step_dict, logger,url):
    # 执行第一个工作流
    if "5" in step_dict.keys():
        json_file = WORKFLOW_JSONPATH_21
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)

        # 获取帧数
        total_frame = min(common_funcs.get_frame_count(win_video_path),480)
        # 跳过帧数
        skip_frame = 0
        lap_counter = 0
        while skip_frame < total_frame:

            # 指定视频路径  video
            prompt["584"]["inputs"]["string"] = centos_video_path
            # 指定基本路径
            prompt["109"]["inputs"]["string"] = base_path
            # Batch Range
            prompt["583"]["inputs"]["seed"] = 120
            # Lap Counter
            prompt["585"]["inputs"]["seed"] = lap_counter

            lap_counter += 1
            skip_frame = lap_counter * 120

            # 调用json文件
            queue_prompt(prompt, url)

    if "6" in step_dict.keys():
        # 执行第二个工作流
        json_file = WORKFLOW_JSONPATH_22
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)

        for skip_frame, batch_range in get_batchs(240,    win_video_path):
            # 指定基本路径
            prompt["86"]["inputs"]["string"] = base_path
            # 修改输入参数 Skip Frame
            prompt["123"]["inputs"]["int"] = skip_frame
            # Batch Range
            prompt["122"]["inputs"]["int"] = batch_range

            # 调用json文件
            queue_prompt(prompt, url)


# 视频转动漫  3
def exec_workflow_video2video_03(win_video_path, video_name,  step_dict, logger, url):

    if "7" in step_dict.keys():
        # 执行第二个工作流
        json_file = WORKFLOW_JSONPATH_31
        with open(json_file, 'r', encoding='utf-8') as jsonFile:
            prompt = json.load(jsonFile)

        for skip_frame, batch_range in get_batchs(240,    win_video_path):
            # 指定要处理的视频名称
            prompt["136"]["inputs"]["string"] = video_name
            # 修改输入参数 Skip Frame
            prompt["123"]["inputs"]["int"] = skip_frame
            # Batch Range
            prompt["122"]["inputs"]["int"] = batch_range
            # 指定输出视频帧率
            # prompt["165"]["inputs"]["Number"] = 60
            # 指定输出视频文件的前缀
            prompt["162"]["inputs"]["string"] = "alan_{}".format(video_name.replace(".mp4", ""))


            # 调用json文件
            queue_prompt(prompt, url)







if __name__ == '__main__':
    # 视频转绘
    step_dict = {
        # "1": "preprocessing",
        # "2": "Raw",
        # "3": "Refined",
        # "4": "FaceFix",
        # "5": "01_源视频处理",
        # "6": "02_视频转绘",
        "7": "视频转动漫",

    }
   # exec_workflow_video2video(video_path,base_path)
    
   # 动画 2

   # 先执行 get_comfyui_video.py 这个脚本文件获取要处理的视频并写入到 data/comfyui_video_info.txt
   # 检查文件中的视频是不是都要处理的视频
    # infos = []
    # url = URL.format(
    #     "https://0679a5ae3a5648cfb5d601dd7e80734bvscpv1v92s.ds.megaease.cn")
    # log_file = '20240501.log'
    # logger = setup_logger(log_file)
    # with open("data/comfyui_video_info.txt", 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         line = line.strip()
    #         if line:
    #             logger.info(f"开始处理视频：{line}")
    #             win_video_path = line
    #             base_name = os.path.basename(line)
    #             file_name, _ = os.path.splitext(base_name)
    #             base_path = f"/root/workspace/{file_name}"
    #             centos_video_path = f"/root/workspace/src/{base_name}"
    #             exec_workflow_video2video_02(win_video_path=win_video_path,
    #                                          centos_video_path=centos_video_path,
    #                                          base_path = base_path, 
    #                                          step_dict = step_dict, 
    #                                          logger=logger,
    #                                          url=url)
    #             logger.info(f"视频提交完成：{line}")
    #             infos.append((base_path, file_name))

    # 视频合并
    # infos = [("/root/workspace/out","out")]
    # for base_path, file_name in infos:
    #     logger.info(f"开始合并视频：{file_name}.mp4")
    #     exec_workflow_combinevideo(
    #         base_path=base_path, images="/Renders/Refined", video_filename=file_name, url=url, frame_rate=30)
    #     logger.info(f"视频合并完成：{file_name}.mp4")

    url = URL.format(
        "https://518029666c884d0ea3911de8bface496vscpv1v92s.ds.megaease.cn")
    log_file = '20240502.log'
    logger = setup_logger(log_file)
    with open("data/comfyui_video_info.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                logger.info(f"开始处理视频：{line}")
                win_video_path = line
                base_name = os.path.basename(line)
                exec_workflow_video2video_03(win_video_path=win_video_path,
                                             video_name=base_name,
                                             step_dict=step_dict,
                                             logger=logger,
                                             url=url)
                logger.info(f"视频提交完成：{line}")
    
