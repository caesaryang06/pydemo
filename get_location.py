import pyautogui
import time

# 给用户5秒时间将鼠标移动到推文输入框的位置
print("Move your mouse over the tweet box and wait.")
time.sleep(7)

# 获取并打印鼠标当前的屏幕坐标
x, y = pyautogui.position()
print(f"The position of the tweet box is: {x}, {y}")
