import webbrowser
import pyautogui
import time
import pyperclip
import string
import random
import keyboard


def generate_custom_username(min_length=6, max_length=12):
    """生成符合习惯的随机用户名"""
    words = ["cool", "fast", "smart", "joy", "tech", "pro",
             "super", "user", "guru", "ninja", "master", "happy"]
    special_chars = ['_', '.']

    # 随机选择一个单词开始
    username = random.choice(words)

    # 随机添加一些小写字母
    num_letters = random.randint(
        1, max_length - len(username) - 2)  # 保留空间给数字和特殊字符
    username += ''.join(random.choices(string.ascii_lowercase, k=num_letters))

    # 可选地添加一个特殊字符
    if random.choice([True, False]):  # 50%的机会
        username += random.choice(special_chars)

    # 添加一些数字来完成用户名
    num_digits = max_length - len(username)
    username += ''.join(random.choices(string.digits, k=num_digits))

    # 检查用户名长度是否符合要求，若不符合则重新生成
    if len(username) < min_length:
        return generate_custom_username(min_length, max_length)

    return username




def register():
    # 打开网页
    webbrowser.open(
        'https://account.proton.me/mail/signup?plan=free&ref=mail_plus_intro-mailpricing-2&currency=USD')
    time.sleep(15)

    # 定位到用户名输入框  742, 501
    pyautogui.click(x=742, y=501)
    # 输入用户名
    username = generate_custom_username()
    password = "NOga056362@"
    pyperclip.copy(username)
    pyautogui.hotkey('ctrl', 'v')

    # 按tab两次
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')

    # 输入密码
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')

    # 按tab一次 再按密码
    pyautogui.press('tab')
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')

    # 定位到注册按钮
    pyautogui.press('tab')
    pyautogui.press('enter')

    return username, password


def main(number):
    with open('usernames.txt', 'a') as f:
        for _ in range(number):
            time.sleep(10)
            username, password = register()
            f.write(f"{username}@proton.me\n")
            print("Press any key to continue...")
            # 等待按任意键
            keyboard.wait()
            print("Continued!")







if __name__ == '__main__':
    main(10)
