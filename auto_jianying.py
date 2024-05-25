import json
import tools.customer_common_funcs as ccf
import shutil
import time


# 函数  获取 common_keyframes
def get_common_keyframes(start_time, end_time,start_scala,end_scala):
    """
    
    :param start_time: 开始时间
    :param end_time: 结束时间
    :param start_scala: 开始缩放大小
    :param end_scala: 结束缩放大小
    """
    with open('jianying/keyframe/template.json', 'r') as file:
        common_keyframes = json.load(file)


    # 对 common_keyframes 进行处理  图片关键帧起始点
    common_keyframes[0]["id"] = ccf.get_uuid()
    common_keyframes[0]["keyframe_list"][0]["id"] = ccf.get_uuid()
    common_keyframes[0]["keyframe_list"][0]["time_offset"] = start_time
    # 缩放大小  100%
    common_keyframes[0]["keyframe_list"][0]["values"] = [start_scala]

    # 对 common_keyframes 进行处理  图片关键帧结束点
    common_keyframes[0]["keyframe_list"][1]["id"] = ccf.get_uuid()
    # 偏移2秒
    common_keyframes[0]["keyframe_list"][1]["time_offset"] = end_time
    # 缩放大小  160%
    common_keyframes[0]["keyframe_list"][1]["values"] = [end_scala]








# 读取json文件并备份修改内容后覆盖源文件
    with open('jianying/keyframe/template.json', 'w') as file:
        json.dump(common_keyframes, file, indent=4) 
        
    return common_keyframes


def main_keyframe(jsonPath):

    # 获取当前时间戳
    current_time = ccf.get_current_timestamp()
    # 备份json文件
    backJsonPath = jsonPath.replace("draft_content.json", f"draft_content_backup_{current_time}.json")
    shutil.copyfile(jsonPath, backJsonPath)

    
    # 读取json文件
    with open(jsonPath, 'r', encoding='utf-8') as file:
        json_data = json.load(file)



    # 先处理主轨道   主轨道是 160%  ~  100% 
    segments_0 = json_data["tracks"][0]["segments"]
    for i in segments_0:
        i["common_keyframes"] = get_common_keyframes(0, 1000000, 1.6, 1.0)



    # 处理主轨道上的第一个轨道
    segments_1 = json_data["tracks"][1]["segments"]
    for i in segments_1:
        i["common_keyframes"] = get_common_keyframes(0, 1000000, 1.0, 0.62)  

    # 将修改后的json对象  json_data 覆盖写入文件 jsonPath     
    with open(jsonPath, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)





if __name__ == '__main__':

    DRAFT_PATH_TEMP = "C:/Users/yangxinmin/AppData/Local/JianyingPro/User Data/Projects/com.lveditor.draft/{}/draft_content.json"
    draft_name = "4月2日"
    jsonPath = DRAFT_PATH_TEMP.format(draft_name)

    main_keyframe(jsonPath)