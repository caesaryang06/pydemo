import webbrowser
import pyautogui
import time
import pyperclip



def main(location_dict,images_list):

    # 打开浏览器
    task_x, task_y = location_dict["1"]
    pyautogui.moveTo(task_x, task_y)
    pyautogui.click()
    browser_x, browser_y = location_dict["2"]
    pyautogui.moveTo(browser_x, browser_y)
    pyautogui.click()
    time.sleep(3)


    # 点击上传按钮并上传图片
    upload_x,upload_y = location_dict["3"]
    pyautogui.moveTo(upload_x,upload_y)
    pyautogui.click()
    time.sleep(5)
    image_name = image_list[0]
    pyautogui.write(image_name)
    pyautogui.press('enter')
    time.sleep(15)
    print(f"{image_name} 图片上传完成")




if __name__ == '__main__':

    # 任务栏浏览器坐标   1143, 1055
    task_x, task_y = 1143, 1055

    #浏览器小窗口坐标
    browser_x, browser_y = 1093, 935

    # 上传按钮的坐标
    upload_x, upload_y = 967, 546


    location_dict = {
        "1": (task_x,task_y),
        "2": (browser_x, browser_y),
        "3": (upload_x, upload_y)
    }


    # 图片列表
    image_list = ["ComfyUI_temp_odvxm_00015_.png"]

    main(location_dict=location_dict,images_list=image_list)
