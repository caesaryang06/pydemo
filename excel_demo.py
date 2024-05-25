import pandas as pd
import tools.customer_common_funcs as ccf
import os 


# info = {
#         '模版名': ['Alice', 'Bob', 'Charlie'],
#         '模版内容': ['New York', 'London', 'Paris']
#     }


# pd.DataFrame(info).to_excel('data/template.xlsx',
#                             index=False, engine='openpyxl')


# df = pd.read_excel('data/template.xlsx', engine='openpyxl')


# b_value = df[df['模版名'] == '生成可爱猫咪分镜图提示词']['模版内容'].values[0]

# print(b_value)


 

# newData = pd.DataFrame({'模版名': ['David'], '模版内容': ['Tokyo']})

# print(data)

# result = pd.concat([data,newData],ignore_index=True)

print("*"*50)
# print(result)


# data.to_excel('data/template.xlsx',
#                             index=False, engine='openpyxl')


# 测试音频文件分割多段  
# ccf.split_audio('aa.MP3', 'out', 90)


# 删除指定文件夹下的所有内容
# ccf.delete_folder_contents('out/audio/tmp')

# str = "d:\vscode-pro\py_demo\tabs\tab5_info.py"


# directory, filename = os.path.split(str)
# path, _ = os.path.split(directory)

# print(path)

import re
def process_text(input_text):
    """  
    处理文本，去除特定格式，并合并成一段。  
      
    参数:  
    input_text (str): 待处理的文本。  
      
    返回:  
    str: 处理后的文本。  
    """

    # 按照空行进行分割
    blocks = re.split(r'\n\s*\n', input_text)
    list = []
    for block in blocks:
        # 按行分割文本
        lines = block.split('\n')

        # 过滤掉以三个###开头的行
        filtered_lines = [line for line in lines if not line.startswith('###')]

        # 去除每行开头的 "处理前字符串：" 和行尾的 "-"
        processed_lines = [line.strip().replace("处理前字符串：", "").rstrip("-")
                        for line in filtered_lines]

        # 合并处理后的行成一个字符串，并去除多余的空格
        output_text = ' '.join(processed_lines).strip()

        # 添加到数组中
        list.append(output_text.replace("**", "").replace("-", "").strip())

    return list


# 示例使用
input_text = """  
处理前字符串：  
### 第一分镜：穿上设计师服装  
- **场景**: 后台化妆间，四周挂满了五光十色的灯光，设计师们忙碌地调整服装。  
- **毛球的形象**: 可爱的猫咪毛球站在化妆镜前，身穿一件精致的设计师服装，这件服装色彩斑斓，带有异域风情的图案。  
- **毛球的动作和表情**: 毛球表情稍显紧张，但也流露出一丝兴奋。它试图用爪子调整衣服上的小装饰，动作拟人化且略显笨拙，让人忍俊不禁。 

### 第四分镜：观众欢呼喝彩
- **场景**: T台的末端，聚光灯聚焦在毛球身上，背景是模糊的欢呼观众。
- **毛球的形象**: 毛球穿着本场秀的压轴服装，这件服装集设计之大成，华美而不失优雅。
- **毛球的动作和表情**: 毛球站在T台的末端，挥动爪子向观众致谢，表情是惊喜交加，尾巴摇摆频频，完全沉醉在这片刻的荣耀中。 
"""

# print(process_text.__doc__)

# output_text = process_text(input_text)
# print("处理后的文本：")
# print(output_text)


# ccf.split_video("aa.mp4","test",10)


# ccf.srt_to_txt("out/subtitle/tmp/cc.srt", "out/subtitle/tmp/cc.txt")
# ccf.srt_to_txt("out/subtitle/tmp/dd.srt", "out/subtitle/tmp/dd.txt")


import datetime

today = datetime.date.today()


print(str(today).replace("-", ""))











