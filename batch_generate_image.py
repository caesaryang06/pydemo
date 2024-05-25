import webbrowser
import pyautogui
import time
import pyperclip


"""
控制comfyui批量出图

"""


def open_compyui_exec(input_box_x, input_box_y, prompt_file, base_url=None, generate_button_x=None,generate_button_y=None):

    if base_url:
        webbrowser.open(base_url)
        time.sleep(5)  # Wait for the browser to open and load the page


    #TODO 加载指定模版


    ## 读取提示词所在文件并遍历提示词列表
    with open(prompt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:

            print(f"开始处理提示词: {line}")

            # 获取x输入框的位置
            pyautogui.moveTo(input_box_x, input_box_y)
            pyautogui.click()

            # 选中输入框中的内容并删除
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'x')

            line = line.strip()
            # 输入提示词
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl', 'v')


            if generate_button_x and generate_button_y:
                pyautogui.moveTo(generate_button_x, generate_button_y)
                pyautogui.click()
            else:
                # 移动到生成按钮位置
                for _ in range(10):
                    pyautogui.press('tab')
                    # Adding a small delay between each 'Tab' press can sometimes improve reliability
                    time.sleep(0.5)

                # 按回车键
                pyautogui.press('enter')


            time.sleep(4)  # 等待生成
 
            print(f"已提交生成提示词: {line}")



if __name__ == '__main__':

    # 指定提示词文件名
    file_name = "batch_prompt.txt"

    # 指定屏幕输入框 (input_box_x, input_box_y）即对应提示词输入框的位置   587, 464
    input_box_x = 610
    input_box_y = 533

    base_url = "http://127.0.0.1:8188/"

    # 生成按钮的位置    1802, 256
    generate_button_x = 1802
    generate_button_y = 256


    open_compyui_exec(input_box_x, input_box_y, file_name, base_url=None, generate_button_x=generate_button_x, generate_button_y=generate_button_y)
