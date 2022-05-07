# Discord自动聊天机器人，撸白名单必备！保姆级教程！

# 安装python3.9.   [Python官方下载](https://www.python.org/) 
学习一点python知识，知道怎么看懂脚本、改简单的脚本、跑脚本

# 打开以下链接，复制代码。
https://github.com/OpenseaSearch/discord_chatbot/blob/main/discord_bot.py

将代码保存为 discord_bot.py 文件。然后打开本地代码文件开始配置参数。

# 这个方法里的值是随机发言的内容，可以按照格式自己修改：
>import requests, random

>def gen_context():
>    context_list = [
>        "hello bro", "let's go !", "to the moon!", "nice", "project", "have a good day",
>        "good", "luck", "how's going", "so do i", "yeah", "same to me", "1", "cool", "so far so good",
>        "hi~", "of course", "really", "cool~", "ok", "what?", "why?", "not bad", "well done", "great",
>       "perferct", "thanks", "ture", "yes", "no", "here", "interesting", "it's funny", "i am tired"
>    ]
>    text = random.choice(context_list)
>    return text

context_list里面就是准备好的剧本，机器人会随机发送一条。

get_context方法是随机获取频道中别人的发言然后发送，代码里用的是这个方法。需要发自己剧本的就改成gen_context这个方法。

# 打开网页版discord获取需要配置的参数：
chanel_list = ['891977019544457260'] #配置chanelId，891977019544457260是研习社chainclub大家庭的channelid。多个值的话要用半角英文的逗号隔开，这样写：chanel_list = ['891977019544457260','891977019544457260']
