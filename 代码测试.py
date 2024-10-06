import pandas as pd
import random


## 定义函数  新增邮箱
def add_email(email, password):
    df = pd.read_excel('data/email.xlsx')
    df.loc[len(df.index)] = [email, password]

    # 对数据去重
    df.drop_duplicates(subset=['邮箱地址'], keep='first', inplace=True)

    # 保存数据
    df.to_excel('data/email.xlsx', index=False)





## 定义函数  删除邮箱
def delete_email(email):
    df = pd.read_excel('data/email.xlsx')
    df.drop(df[df['邮箱地址'] == email].index, inplace=True)

    # 保存数据
    df.to_excel('data/email.xlsx', index=False)




## 定义函数  列出所有软件
def list_software():
    df = pd.read_excel('data/software.xlsx')
    
    # software.xlsx 中  第一列为软件名称 第二列为邮箱名称   第三列为状态
    # 列出所有软件名称
    software_list = df['软件名称'].tolist()
    return software_list


# 定义函数  新增软件  第一列为软件名称 第二列为邮箱名称   第三列为状态
def add_software(software_name, email):
    df = pd.read_excel('data/software.xlsx')

    # 这里需要判断  如果 df 存在 软件名称 和 邮箱名称 相同的记录 则更新对应的记录 如果不存在 则添加
    if (df[(df['软件名称'] == software_name) & (df['邮箱地址'] == email)].empty):
        df.loc[len(df.index)] = [software_name, email, 'enable']
    else:
        df.loc[(df['软件名称'] == software_name) & (df['邮箱地址'] == email), '状态'] = 'enable'

    # 对数据去重
    df.drop_duplicates(subset=['软件名称', '邮箱地址'], keep='first', inplace=True)

    # 保存数据
    df.to_excel('data/software.xlsx', index=False)



# 定义函数  修改软件状态为 disable  第一列为软件名称 第二列为邮箱名称   第三列为状态    
def disable_software(software_name, email):
    df = pd.read_excel('data/software.xlsx')
    df.loc[(df['软件名称'] == software_name) & (df['邮箱地址'] == email), '状态'] = 'disable'

    #  按照 软件名称 和 邮箱名称 去重
    df.drop_duplicates(subset=['软件名称', '邮箱地址'], keep='first', inplace=True)

    # 保存数据 
    df.to_excel('data/software.xlsx', index=False)


# 定义函数 根据软件名称  查看可用的邮箱地址  第一步先看 software.xlsx 这里面是否有对应的软件名称  如果有 列出所有不可用的邮箱  然后从 email.xlsx 中读取所有邮箱并过滤掉不可用的邮箱之后随便返回一个
def get_email(software_name):
    df_software = pd.read_excel('data/software.xlsx')
    df_email = pd.read_excel('data/email.xlsx')

    # 先看 software.xlsx 里面是否有对应的软件名称
    if software_name in df_software['软件名称'].tolist():
        # 列出所有不可用的邮箱
        disable_email_list = df_software[df_software['状态'] == 'disable']['邮箱地址'].tolist()
        
        # 从 email.xlsx 中读取所有邮箱并过滤掉不可用的邮箱
        enable_email_list = df_email[~df_email['邮箱地址'].isin(disable_email_list)]['邮箱地址'].tolist()
        
        # 随便返回一个
        return random.choice(enable_email_list)


# 定义函数 先判断 software.xlsx 中存在软件名称为 aa  且 状态为enable 的邮箱 如果存在 则取出第一个软件名称为 aa 且状态为 enable的邮箱
def get_email_by_software_name(software_name):
    df = pd.read_excel('data/software.xlsx')
    email = df[(df['软件名称'] == software_name) & (df['状态'] == 'enable')]['邮箱地址'].tolist()
    if email:
        return email[0]
    else:
        return None
    




if __name__ == '__main__':
    # # 列出所有软件
    # print(list_software())

    # # 新增软件
    # add_software('cursor', 'caesaryang06@163.com')
    
    print(get_email_by_software_name('app.runwayml.com'))
    str = "abd"

    info = f"""
    aa: {str}


"""
