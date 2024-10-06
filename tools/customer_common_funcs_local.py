import os
import time
import pyautogui








# 打开指定页面函数传入位置字典
def open_page(page_dict):
    # 鼠标定位到任务栏指定软件

    # 判断传入的字典中是否包含1这个key
    if '1' in page_dict:
        location_1_x, location_1_y = page_dict['1']
        pyautogui.moveTo(location_1_x, location_1_y)
        pyautogui.click()

    time.sleep(1)
    # 判断传入的字典中是否包含2这个key
    if '2' in page_dict:
        location_2_x, location_2_y = page_dict['2']
        pyautogui.moveTo(location_2_x, location_2_y)
        pyautogui.click()

    time.sleep(1)



    """
    返回指定路径下的所有文件名称

    Args:
    directory_path (str): The path to the directory from which to list files.

    Returns:
    list: A list of file names in the directory.
    """
    file_names = []  # Initialize an empty list to store file names
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)  # Create full path
        if os.path.isfile(file_path):  # Check if it is a file
            file_names.append(filename)
    return file_names


