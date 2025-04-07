# -*- coding: utf-8 -*-
"""
模拟的调用方
"""

import requests

# url = "http://127.0.0.1:9001/predict"
url = "http://118.178.255.229:9001/predict"


def t1():
    # 获取url对应的执行结果
    response = requests.post(url, json={'text': '我是小明3', 'k': 3})
    if response.status_code == 200:
        print("访问服务器成功")
        # 明确的知道服务器返回的是json格式，那么可以直接调用json()这个方法转换为字典对象
        result = response.json()
        print(result)
        if result['code'] == 0:
            print(f"调用模型成功，结果为:{result['data']}")
        else:
            print(f"调用模型服务器处理异常，异常信息为:{result['msg']}")
    else:
        # https://www.jianshu.com/p/43ac46a8fcdb
        print(f"访问服务器失败：网络异常等等:{response.status_code}")


if __name__ == '__main__':
    t1()
