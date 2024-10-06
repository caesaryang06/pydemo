import webbrowser
import pyautogui
import time
import pyperclip
import tools.customer_common_funcs_local as common_funcs

"""
控制discord中的domoai执行

"""


# main video
def main_text2img(data_path):
    # 定义位置字典
    locations_dict = {
        "1": (651, 1040),  # 激活软件的第一级位置信息
       # "2": (272, 927),  # 激活软件的第二级位置信息
        "3": (552, 950),  # 输入框的位置信息
    }


    # 打开浏览器
    common_funcs.open_page(locations_dict)

   # 打开输入文件并按行读取所有内容
    with open(data_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 遍历每一行
    for line in lines:
        # 去除行尾的换行符
        line = line.strip().replace('/imagine prompt: ', '')

        # 打印要处理的提示词
        print(f"正在处理提示词: {line}")

        # 定位输入框并输入提示词
        pyautogui.click(locations_dict["3"])
        # 复制行内容到剪贴板
        pyperclip.copy("/imagine")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        time.sleep(5)
        pyperclip.copy(line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

        time.sleep(7)


def main(os_type,  data_path):
    if os_type == "text2imag":
        main_text2img( data_path)



if __name__ == '__main__':


    # 操作类型  单纯的通过提示词输出图片
    op_info_dict = {
        "1": ["text2imag", "data/mj_prompt.txt"],
    }

    os_type, data_path = op_info_dict["1"]
    main(os_type=os_type,data_path=data_path)
