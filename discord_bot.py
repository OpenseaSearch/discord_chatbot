# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/3 19:18
@Auth ： d1rrick DanielGao.eth
@File ：autochat.py
@IDE ：vscode

"""
import requests
import json
import random
import time
import re


def gen_context():
    context_list = [
        "hello bro", "let's go !", "to the moon!", "nice", "project", "have a good day",
        "good", "luck", "how's going", "so do i", "yeah", "same to me", "1", "cool", "so far so good",
        "hi~", "of course", "really", "cool~", "ok", "what?", "why?", "not bad", "well done", "great",
        "perferct", "thanks", "ture", "yes", "no", "here", "interesting", "it's funny", "i am tired"
    ]
    text = random.choice(context_list)
    return text


def get_context():
    chanel_list = ['891977019544457260']
    headr = {
        "Authorization": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    chanel_id = random.choice(chanel_list)
    url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(
        chanel_id)
    res = requests.get(url=url, headers=headr)
    result = json.loads(res.content)
    result_list = []
    for context in result:
        if ('<') not in context['content']:
            if ('@') not in context['content']:
                if ('http') not in context['content']:
                    if ('?') not in context['content']:
                        result_list.append(context['content'])

    return random.choice(result_list)


def chat():
    chanel_list = ['891977019544457260']
    authorization_list = [
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx']
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        for chanel_id in chanel_list:
            msg = {

                "content": get_context(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False

            }
            url = 'https://discord.com/api/v9/channels/{}/messages'.format(
                chanel_id)
            try:
                res = requests.post(url=url, headers=header,
                                    data=json.dumps(msg))
                print(res.content)
            except Exception:
                print(Exception)
            continue
        # 取30秒到50之间的一个随机数，作为循环的间隔时间。
        time.sleep(random.randrange(30, 50))


if __name__ == '__main__':
    while True:
        try:
            print('start')
            chat()
            # 取180秒到240之间的一个随机数，作为机器人发送消息的间隔时间。
            sleeptime = random.randrange(180, 240)
            time.sleep(sleeptime)
        except:
            pass
        continue
