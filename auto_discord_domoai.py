import webbrowser
import pyautogui
import time
import pyperclip
import tools.customer_common_funcs as common_funcs

"""
控制discord中的domoai执行

"""

# 获取指定路径下的所有文件名称并写入到指定文件中
def get_all_file_names_and_write_to_file(file_path, write_file_path):
    file_names = common_funcs.list_files_in_directory(file_path)
    with open(write_file_path, 'w') as f:
        f.write('\n'.join(file_names))


# domoai  video2video
def open_discord_exec_domoAI_video2video(media_path, prompt, locations_dict):

    # 激活discord客户端
    discord_location_x, discord_location_y = locations_dict['1']
    pyautogui.moveTo(discord_location_x, discord_location_y)
    pyautogui.click()
    time.sleep(5)  # 等待discord客户端加载

    # 遍历视频并处理
    with open(media_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            print(f"开始处理视频: {line}")

            #  单击机器人交互的输入框   523, 961
            input_box_x, input_box_y = locations_dict['2']
            pyautogui.moveTo(input_box_x, input_box_y)
            pyautogui.click()
            time.sleep(4)

            # 输入video
            pyperclip.copy("/video")
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
    
            # 按回车键
            pyautogui.press('enter')
            time.sleep(5)

            # 点击上传视频的位置
            upload_video_x, upload_video_y = locations_dict['3']
            pyautogui.moveTo(upload_video_x, upload_video_y)
            pyautogui.click()
            time.sleep(5)

            # 选择视频文件并上传
            pyperclip.copy(line)      
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            # Wait for the image to upload
            time.sleep(20)  

            for _ in range(2):
                pyautogui.press('tab')
                time.sleep(0.5)
           # 输入提示词    dancing --port --ani v1
            pyperclip.copy(prompt)
            pyautogui.hotkey('ctrl', 'v')

            time.sleep(3)
            pyautogui.press('enter')

            # 提交后进行交互 需要多等待一会
            time.sleep(60)

            # 移动到生成10s的位置并单击
            generate_button_x, generate_button_y = locations_dict['4']
            pyautogui.moveTo(generate_button_x, generate_button_y)
            pyautogui.click()
            time.sleep(15)

            # 移动到开始按钮并单击
            start_button_x, start_button_y = locations_dict['5']
            pyautogui.moveTo(start_button_x, start_button_y)
            pyautogui.click()
            time.sleep(60)

            print(f"视频处理完成: {line}")


# domoai  img2video
def open_discord_exec_domoAI_img2video(media_path, prompt, locations_dict):

    # 激活discord客户端
    discord_location_x, discord_location_y = locations_dict['1']
    pyautogui.moveTo(discord_location_x, discord_location_y)
    pyautogui.click()
    time.sleep(5)  # 等待discord客户端加载

    # 遍历视频并处理
    with open(media_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            print(f"开始处理图片: {line}")

            #  单击机器人交互的输入框   523, 961
            input_box_x, input_box_y = locations_dict['2']
            pyautogui.moveTo(input_box_x, input_box_y)
            pyautogui.click()
            time.sleep(4)

            # 输入video
            pyperclip.copy("/animate")
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

            # 按回车键
            pyautogui.press('enter')
            time.sleep(5)

            # 点击上传图片的位置
            upload_img_x, upload_img_y = locations_dict['3']
            pyautogui.moveTo(upload_img_x, upload_img_y)
            pyautogui.click()
            time.sleep(5)

            # 选择图片文件并上传
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            # Wait for the image to upload
            time.sleep(20)

        #     for _ in range(4):
        #         pyautogui.press('tab')
        #         time.sleep(0.5)
        #     pyautogui.press('enter')
        #     time.sleep(5)
        #    # 输入提示词    dancing --port --ani v1
        #     pyperclip.copy(prompt)
        #     pyautogui.hotkey('ctrl', 'v')

            time.sleep(3)
            pyautogui.press('enter')
            pyautogui.press('enter')
            # 提交后进行交互 需要多等待一会
            time.sleep(30)


            # 移动到中等强度按钮的位置
            pyautogui.moveTo(682, 758)
            pyautogui.click()
            time.sleep(15)

            # 移动到生成5s按钮的位置
            pyautogui.moveTo(857, 812)
            pyautogui.click()
            time.sleep(15)

            # 移动到开始按钮并单击
            start_button_x, start_button_y = locations_dict['4']
            pyautogui.moveTo(start_button_x, start_button_y)
            pyautogui.click()
            time.sleep(30)

            print(f"图片处理完成: {line}")




# main video
def main_vidoe2video(prompt,media_path):
    # 指定discord在任务栏的位置  1144, 1053
    discord_location_x = 1144
    discord_location_y = 1053

    # 指定输入框的位置  523, 961
    input_box_x = 523
    input_box_y = 961

    # 上传视频的位置  566, 768
    upload_video_x = 566
    upload_video_y = 768

    # 生成10s视频按钮的位置  1240, 804
    generate_button_x = 1240
    generate_button_y = 804

    # 开始按钮的位置   519, 847 
    start_button_x = 519
    start_button_y = 847

    # 定义位置字典
    locations_dict = {
        "1": (discord_location_x, discord_location_y),
        "2": (input_box_x, input_box_y),
        "3": (upload_video_x, upload_video_y),
        "4": (generate_button_x, generate_button_y),
        "5": (start_button_x, start_button_y)
    }

    open_discord_exec_domoAI_video2video(media_path=media_path, prompt=prompt,
                             locations_dict=locations_dict)


# main img
def main_img2video(prompt, media_path):
    # 指定discord在任务栏的位置  1144, 1053
    discord_location_x = 1144
    discord_location_y = 1053

    # 指定输入框的位置  523, 961
    input_box_x = 523
    input_box_y = 961

    # 上传图片的位置  566, 768
    upload_img_x = 566
    upload_img_y = 768

    # 开始按钮的位置   519, 847
    start_button_x = 519
    start_button_y = 847

    # 定义位置字典
    locations_dict = {
        "1": (discord_location_x, discord_location_y),
        "2": (input_box_x, input_box_y),
        "3": (upload_img_x, upload_img_y),
        "4": (start_button_x, start_button_y)
    }

    open_discord_exec_domoAI_img2video(media_path=media_path, prompt=prompt,
                                         locations_dict=locations_dict)
  


def main(os_type, prompt, media_path):
    if os_type == "img2video":
        main_img2video(prompt, media_path)
    elif os_type == "video2video":
        main_vidoe2video(prompt, media_path)





if __name__ == '__main__':

    prompt_dict = {

        # 视频转绘提示词
        "视频经典台词提示词": "talking --land --illus v1.1"        
        , "视频跳舞提示词": "dancing --port --ani v1"


        # 图片生成视频提示词 
        , "图片提示词": "cat"   # img2video 提示词
    }

    
    # 操作类型  img2video video2video
    op_info_dict = {
        "1": ["img2video", "data/domoai_img.txt"]        
        , "2": ["video2video", "data/domoai_video.txt"]
    }


    # 获取指定路径下的所有文件名称并写入到指定文件中
    get_all_file_names_and_write_to_file(
        file_path="C:/Users/yangxinmin/Desktop/workspace/切割后的视频片段", write_file_path="data/domoai_video.txt")

    os_type, media_path = op_info_dict["2"]
    main(os_type=os_type, prompt=prompt_dict['视频经典台词提示词'], media_path=media_path)
