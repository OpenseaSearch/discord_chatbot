# discord_chatbot
Discord自动聊天机器人，撸白名单必备！


如有python环境，请下载未编译版本进行使用
请完整复制所有代码，然后在本地保存为.py文件。注意所有标点符号必须是半角英文格式

如没有python环境，请下载已编译版本进行使用，解压密码：__discord_bot__


将代码保存为 discord_bot.py 文件。然后打开本地代码文件开始配置参数。

这个方法里的值是随机发言的内容，可以按照格式自己修改：
import requests, random

def gen_context():
    context_list = [
        "hello bro", "let's go !", "to the moon!", "nice", "project", "have a good day",
        "good", "luck", "how's going", "so do i", "yeah", "same to me", "1", "cool", "so far so good",
        "hi~", "of course", "really", "cool~", "ok", "what?", "why?", "not bad", "well done", "great",
        "perferct", "thanks", "ture", "yes", "no", "here", "interesting", "it's funny", "i am tired"
    ]
    text = random.choice(context_list)
    return text
context_list里面就是准备好的剧本，机器人会随机发送一条。

get_context方法是随机获取频道中别人的发言然后发送，代码里用的是这个方法。需要发自己剧本的就改成gen_context这个方法。

打开网页版discord获取需要配置的参数：
chanel_list = ['891977019544457260'] #配置chanelId，891977019544457260是研习社chainclub大家庭的channelid。多个值的话要用半角英文的逗号隔开，这样写：chanel_list = ['891977019544457260','891977019544457260']

获取chanelID：



获取Authorization：

按 f12 打开浏览器的开发者工具：

然后选择 network（或者 网络 ）标签之后，再发送任意内容到频道内：第二步要点击一条 post 请求。然后在第四步拿到Authorization值。



将Authorization的值写入代码里以下两个地方。1这里要用半角双引号。2这里要用半角单引号。



每个用户的authorization是唯一的，所以我们可以保存长期使用。chanel_id要根据你发言的频道去取。

好了，参数配置完毕。

接下来在终端中运行即可。
