import webbrowser
import pyautogui
import time
import pyperclip


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def open_twitter_and_tweet(content, tweet_box_x, tweet_box_y, media_path=None):
    webbrowser.open('https://twitter.com/home')
    time.sleep(8)  # Wait for the browser to open and load the page


    ## 获取x输入框的位置
    pyautogui.moveTo(tweet_box_x, tweet_box_y)
    pyautogui.click()

    pyperclip.copy(content)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(1)  # Wait for the content to be pasted

    ## 图片或者视频的路径
    if media_path:
        # Press the 'Tab' key to navigate to the 'Add photos or video' button
        for _ in range(2):
            pyautogui.press('tab')
            # Adding a small delay between each 'Tab' press can sometimes improve reliability
            time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(2)  # Wait for the file dialog to open

        # Type the image path and press 'Enter'
        pyautogui.write(media_path)
        pyautogui.press('enter')

        time.sleep(5)  # Wait for the image to upload


    # Press the 'Tab' key to navigate to the 'Tweet' button
    for _ in range(8):
        pyautogui.press('tab')
        # Adding a small delay between each 'Tab' press can sometimes improve reliability
        time.sleep(0.5)

    # Press the 'Enter' key to click the 'Tweet' button and send the tweet
    pyautogui.press('enter')




if __name__ == '__main__':
    file_name = "Text_to_broadcast.txt"
    content = read_file(file_name)

    media_path = "D:/vscode-pro/py_demo/bb.png"

    # 获取屏幕坐标（tweet_box_x, tweet_box_y）即对应Twitter页面上的推文输入框的位置   723, 215

    # 推特输入框的位置
    tweet_box_x = 723
    tweet_box_y = 215


    open_twitter_and_tweet(content, tweet_box_x, tweet_box_y, media_path)
