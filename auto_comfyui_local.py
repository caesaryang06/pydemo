import json
import requests
import tools.customer_common_funcs as common_funcs


#######################################基础配置#########################################################
URL = "http://127.0.0.1:8188/prompt"
WORKFLOW_BASE_PATH = "D:/vscode-pro/py_demo/workflow"
DATA_BASE_PATH = "C:/Users/yangxinmin/Desktop/workspace/comfyui"

############################################工具########################################################
WORKFLOW_TOOLS_COMBINEVIDEO = f"{WORKFLOW_BASE_PATH}/工具/视频合并.json"




#######################################测试单个流########################################################



#########################################动画###########################################################
WORKFLOW_JSONPATH_01 = f"{WORKFLOW_BASE_PATH}/动画/动画步骤一.json"
WORKFLOW_JSONPATH_02 = f"{WORKFLOW_BASE_PATH}/动画/动画步骤二.json"
WORKFLOW_JSONPATH_03 = f"{WORKFLOW_BASE_PATH}/动画/动画步骤三.json"
WORKFLOW_IMAGE2VIDEO = f"{WORKFLOW_BASE_PATH}/图片生成视频.json"
#######################################################################################################


# 根据视频获取处理批次
def get_batchs(batch_range,video_path):
    result = []
    skip_frame = 0
    total_frame = common_funcs.get_frame_count(video_path)
    while skip_frame < total_frame:
        result.append((skip_frame,batch_range))
        skip_frame += batch_range

    return result

# 动画流执行
def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    response = requests.post(URL, data=data)


# 动画工作流执行
def exec_workflow_01(video_path, base_path, delimiter, batch_range_01, batch_range_02):
    # 执行第一个工作流
    json_file = WORKFLOW_JSONPATH_01
    with open(json_file, 'r', encoding='utf-8') as jsonFile:
        prompt = json.load(jsonFile)

    for skip_frame,batch_range in get_batchs(batch_range_01,video_path):
        # 指定视频路径  video
        prompt["50"]["inputs"]["video"] = video_path
        # 指定基本路径
        prompt["55"]["inputs"]["value"] = base_path
        # 指定路径分隔符
        prompt["65"]["inputs"]["value"] = delimiter
        # 修改输入参数 Skip Frame
        prompt["50"]["inputs"]["skip_first_frames"] = skip_frame
        # Batch Range
        prompt["50"]["inputs"]["frame_load_cap"] = batch_range

        # 调用json文件
        queue_prompt(prompt)


    # 执行第二个工作流
    # json_file = WORKFLOW_JSONPATH_02
    # with open(json_file, 'r', encoding='utf-8') as jsonFile:
    #     prompt = json.load(jsonFile)

    # for skip_frame, batch_range in get_batchs(batch_range_02, video_path):
    #     # 修改输入参数 Skip Frame
    #     prompt["50"]["inputs"]["skip_first_frames"] = skip_frame
    #     # Batch Range
    #     prompt["50"]["inputs"]["frame_load_cap"] = batch_range

    #     # 调用json文件
    #     queue_prompt(prompt)


    # 执行第三个工作流


# 视频合并
def exec_workflow_combinevideo(images,frame_rate=24,filename_prefix="alan"):
    json_file = WORKFLOW_TOOLS_COMBINEVIDEO
    with open(json_file, 'r', encoding='utf-8') as jsonFile:
        prompt = json.load(jsonFile)

    # 指定基本路径
    prompt["158"]["inputs"]["string"] = DATA_BASE_PATH
    # 指定帧率
    prompt["53"]["inputs"]["value"] = frame_rate

    # 指定images1路径
    prompt["159"]["inputs"]["string"] = images
    # 指定视频前缀
    prompt["190"]["inputs"]["string"] = f"{filename_prefix}_{common_funcs.getCurrentDateStr()}"


    # 调用json文件
    queue_prompt(prompt)       


# 视频转动漫
def exec_workflow_video2video():
    # 执行第一个工作流
    json_file = WORKFLOW_JSONPATH_01
    with open(json_file, 'r', encoding='utf-8') as jsonFile:
        prompt = json.load(jsonFile)

    for skip_frame, batch_range in get_batchs(50,    video_path):
        # 指定视频路径  video
        prompt["50"]["inputs"]["video"] = video_path
        # 指定基本路径
        prompt["55"]["inputs"]["value"] = base_path
        # 指定路径分隔符
        prompt["65"]["inputs"]["value"] = delimiter
        # 修改输入参数 Skip Frame
        prompt["50"]["inputs"]["skip_first_frames"] = skip_frame
        # Batch Range
        prompt["50"]["inputs"]["frame_load_cap"] = batch_range

        # 调用json文件
        queue_prompt(prompt)


    pass        


# 单个流测试
def exec_workflow_single(single_workflow_name,prompt_file,filename_prefix):
    json_file = WORKFLOW_BASE_PATH + single_workflow_name
    with open(json_file, 'r', encoding='utf-8') as jsonFile:
        prompt = json.load(jsonFile)
    
    # 遍历提示词进行处理
    with open(prompt_file, 'r', encoding='utf-8') as file:
        contents = file.readlines()
        for content in contents:
            print("开始处理提示词：" + content)
            
            # 指定提示词
            prompt["76"]["inputs"]["string"] = f"{content}"
            # 指定文件前缀
            prompt["74"]["inputs"]["filename_prefix"] = filename_prefix

            # 调用json文件
            queue_prompt(prompt)

            print("提交完成提示词：" + content)




# 图片生成视频工作流执行
def exec_workflow_image2video(image_path, skip_frame, filename_prefix = "alan"):
    # 执行第一个工作流
    json_file = WORKFLOW_IMAGE2VIDEO
    with open(json_file, 'r', encoding='utf-8') as jsonFile:
        prompt = json.load(jsonFile)

    #获取指定路径下图片的个数
    image_counts = common_funcs.count_files(image_path)  

    # 指定图片路径
    prompt["13"]["inputs"]["string"] = image_path
    # 修改输入参数 Skip Frame
    prompt["11"]["inputs"]["skip_first_frames"] = skip_frame
    # Batch Range
    prompt["11"]["inputs"]["image_load_cap"] = image_counts
    # 指定视频前缀    
    prompt["16"]["inputs"]["filename_prefix"] = filename_prefix
                
    # 调用json文件
    queue_prompt(prompt)



if __name__ == '__main__':
    # 视频转绘
    # video_path = "D:/vscode-pro/py_demo/workflow/视频/source_01.mp4"
    # batch_range_01 = 100
    # base_path = "D:/vscode-pro/py_demo/workflow/out"
    # delimiter = "/"
    # exec_workflow_01(video_path, base_path, delimiter, batch_range_01, None)

    # 图片生成视频
    # exec_workflow_image2video(image_path=f"{BASE_PATH}/out/Frame", skip_frame=0, filename_prefix="alan_Frame")
    # exec_workflow_image2video(
    #     image_path=f"{BASE_PATH}/out/OpenPose", skip_frame=0, filename_prefix="alan_Openpose")
    # exec_workflow_image2video(
    #     image_path=f"{BASE_PATH}/out/Softedge", skip_frame=0, filename_prefix="alan_Softedge")

    # 视频合并
    # imagesList = ["/test3/Raw", "/test3/Refined", "/test3/FaceFix"]
    # for images in imagesList:
    #     filename_prefix = images.strip('/').replace('/','_')
    #     exec_workflow_combinevideo(images,frame_rate=30,filename_prefix=filename_prefix)
    
    # 测试单个流
    exec_workflow_single(single_workflow_name="/测试/workflow_api.json", prompt_file="data/workflow_prompt.txt", filename_prefix="alan")