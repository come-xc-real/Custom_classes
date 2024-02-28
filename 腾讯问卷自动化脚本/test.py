import time
import requests
import json
import pandas as pd
import random

url = 'https://wj.qq.com/api/v2/respondent/surveys/14190657/answers?pv_uid=58cc8637-1595-4f1e-92bb-dd489dfd75f6&hash=a0f0&_=1708840623661'  # 你的API端点
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '732',
    'Content-Type': 'application/json',
    "Cookie": "pgv_pvid=1321985730; ptcz=f7225715ca5d7ee4dd224c85d56830ad782ccc1fd63df1307cda27586e8bc306; pac_uid=0_a3c634af046a8; qq_domain_video_guid_verify=a28358141811c326; eas_sid=N1z6Q9D2v4r3W9t9X9M7w3T9S5; fqm_pvqid=1624deae-39c9-41f5-9f65-173245c7076e; RK=CAv5hw6H3k; __wj_userid=58cc8637-1595-4f1e-92bb-dd489dfd75f6; session_user=OTlEWkhJUkQ2Zi9iMWZFNXBmQVlFdz09--in9M5Qigl%2BHAOK7i77Z6Qg%3D%3D--1bd9b390cd4adb6fa4b8b4f7ee984e52; session_respondent=MVhqTjZhQ1ZPSmFmUGZmYmhhYmdYUT09--dAcUc4%2FSlfX%2FmjUqb4VkuQ%3D%3D--83dbdea0c67d78c4911b88abb545969a; answer_session=3e2FOBXJdOM; _session=d2NIZ1BLU3dQNHlQTHNnMHVYaU1wUT09--8bfo7M3GKtCB%2FNHArLafYg%3D%3D--ee6adbfda3a5677e5e4f8f62be2eebe9",
    "Host": "wj.qq.com",
    "Origin": "https://wj.qq.com",
    "Referer": "https://wj.qq.com/s2/14190657/a0f0/",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
with open('test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# 指定要读取的Excel文件路径
# file_path = 'name.xlsx'

# 使用pandas读取Excel文件
# df = pd.read_excel(file_path)

for i in range(100):
    # student_name = row.loc["姓名"]
    # student_id = row.loc["学号"]
    # data["answer_survey"]["pages"][0]["questions"][0]["text"] = student_name
    # data["answer_survey"]["pages"][0]["questions"][1]["text"] = student_id
    i_2 = random.choice([True,True,True,True,True,True,True,True,True, False])
    if i_2:
        data["answer_survey"]["pages"][0]["questions"][0]["options"][0]["id"] = "o-104-687f"  # 喜欢
    else:
        data["answer_survey"]["pages"][0]["questions"][0]["options"][0]["id"] = "o-105-2a31"  # 不喜欢

    i_3 = random.choice([1, 2, 3, 4, 2, 2, 2, 2])
    if i_3 == 1:
        data["answer_survey"]["pages"][0]["questions"][1]["options"][0]["id"] = "o-101-c2c8"
    elif i_3 == 2:
        data["answer_survey"]["pages"][0]["questions"][1]["options"][0]["id"] = "o-102-ad7b"
    elif i_3 == 3:
        data["answer_survey"]["pages"][0]["questions"][1]["options"][0]["id"] = "o-103-763f"
    else:
        data["answer_survey"]["pages"][0]["questions"][1]["options"][0]["id"] = "o-104-3d02"

    i_4 = random.choice([True,True,True,True,True,True,True, False,False,False,])
    if i_4:
        data["answer_survey"]["pages"][0]["questions"][2]["options"][0]["id"] = "o-0-kw2p"
    else:
        data["answer_survey"]["pages"][0]["questions"][2]["options"][0]["id"] = "o-1-lMWJ"
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.text)  # 打印响应内容

