# coding:utf-8

from allData import *
import os

# 技能值
keyOne = '目前技能值：\n<python程序设计>\n<Revit api开发>\n<还有其他乱七八糟的....>\n{}\n[666][666][666]\n\n'.format(
        '-' * 18)


# 关注后回复的消息
@robot.subscribe
def subscribe(message):
    return '/:sun 嘿 你好~\n{}/:sun我现在支持一些有趣的功能\n/:sun比如给我发送的图片中有文字\n/:sun会自动把它识别出来\n/:sun其他功能可以尝试回复\n[666][666][666]\n\n【关键字】\n【好用不火】【资源】'.format(
            keyOne)


# 获取关键词信息
@robot.text
def keyWords(message):
    if message.content == "好用不火" or message.content == "关键字":
        _key = "{}回复下方关键字可以获取有趣的内容：\n格式要求：关键词+空格+内容\n\n".format(keyOne)
        fileName = 'allData/keywords.txt'
        with open(fileName, encoding='utf-8') as f:
            keys = f.read().split()
            for key in keys:
                if key == '*':
                    _key += '------------------\n'
                else:
                    _key += keyStr(key)
            return _key


# 获取关键词信息
@robot.text
def keyWords(message):
    if message.content == "资源" or message.content == "资源下载":
        _key = "{}回复下方关键字可以获取资源下载地址：\n格式要求：关键词\n\n".format(keyOne)
        fileName = 'allData/keydata.txt'
        with open(fileName, encoding='utf-8') as f:
            keys = f.read().split()
            for key in keys:
                if key == '*':
                    _key += '------------------\n'
                else:
                    _key += keyStr(key)
            return _key


# 识别图片中包含的文字内容
@robot.image
def baiduImage(message):
    user_img = message.img
    basicGeneral = client_Baidu.basicGeneralUrl(user_img)
    """ 识别结果数 """
    num = basicGeneral["words_result_num"]
    words = ""
    for word in basicGeneral["words_result"]:
        text = word["words"] + '\n'
        words += text
    '''输出全部文字内容'''
    ruSult = "✨启用图片文字OCR功能\n✨识别结果总行数: {}\n✨文字内容如下:↓↓\n{}\n{}".format(num,
                                                                     '-' * 35,
                                                                     words)
    return ruSult


@robot.filter(re.compile("识别文字.*?"))
def imageOCR(message):
    words = '✨发送一张带文字的图片\n✨自动识别其中的文字'
    return words


# 翻译功能
@robot.filter(re.compile("翻译.*?"))
def translate(message):
    msg = message.content
    byword = msg.strip('翻译').strip().strip('+')
    if byword == '':
        return '✨翻译:自动翻译一段话返回给你\n✨(eg:翻译功能+我叫什么名字)'
    else:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        form_data = {
            "i"          : byword,
            "from"       : " AUTO",
            "to"         : "AUTO",
            "smartresult": "dict",
            "client"     : "fanyideskweb",
            "salt"       : "15611131688671",
            "sign"       : "5811158cc65ce06a3a4ced077ab3839b",
            "ts"         : "1561113168867",
            "bv"         : "9d1e6a4f9d4241fb7947f623cc9e4efa",
            "doctype"    : "json",
            "version"    : "2.1",
            "keyfrom"    : "fanyi.web",
            "action"     : "FY_BY_REALTlME"
        }
        # 请求表单数据
        response = requests.post(url, data=form_data)
        # 将json格式字符串转字典
        content = json.loads(response.text)
        # 打印翻译后得数据
        tgt = content["translateResult"][0][0]["tgt"]
        word = '【{}】翻译结果为：\n{}'.format(byword, tgt)
        return word


# AI搜索引擎
@robot.filter(re.compile("搜索.*?"))
def AIquak(message):
    msg = message.content
    byword = msg.strip('搜索').strip()
    if byword == '':
        return '✨AI搜索优化搜索结果\n✨eg:搜索 内容'
    else:
        word = 'https://quark.sm.cn/s?q=' + byword
        key = '✨关于【{}】的AI搜索'.format(byword)
        words = quark(key, word)
        return words


# 电影下载
@robot.filter(re.compile("电影.*?"))
def movieThunder(message):
    msg = message.content
    word = dytt(msg)
    
    if word != None:
        return word
    else:
        return '✨请输入完成电影名称\n✨资源可能未被收录'


# 小说下载
@robot.filter(re.compile("小说.*?"))
def movieThunder(message):
    msg = message.content
    return xuubook(msg)


# 基金- 增长率情况
@robot.filter(re.compile("fund.*?"))
def fund_JZGS_everyday(message):
    msg = message.content
    # 获取上传素材的临时ID
    media_id = fund_describe_photo(msg)
    if media_id == '✨fund 基金代码\n✨eg:fund 110011（基金代码）':
        return media_id
    else:
        # 回复图片消息
        reply = ImageReply(message=message, media_id=media_id)
        return reply


# 基金-账户-user
@robot.filter(re.compile("user.*?"))
def fund_user_all(message):
    msg = message.content
    return fund_to_client_user(msg)


# 京东比价
@robot.filter(re.compile("比价.*?"))
def fund_JZGS_everyday(message):
    msg = message.content
    return jd_response(msg)


# 微信听歌
@robot.filter(re.compile("music.*?"))
def wx_music(message):
    msg = message.content
    return music_flac(msg)


# revit-插件用户管理
@robot.filter(re.compile("注册插件.*?"))
def toSetRevitAppUser(message):
    msg = message.content
    # 获取验证码
    return getCaptcha(msg)


# 当日基金推荐
@robot.filter(re.compile("xml"))
def readExceltoSendFund(message):
    # 基金推荐
    msg = message.content
    return xmlFundEveryday(msg)


# 基金计算情况
@robot.filter(re.compile("margin.*?"))
def getMargin(message):
    msg = message.content
    return GetFundMoney(msg)


# 基金- 可卖出份额
@robot.filter(re.compile("shell.*?"))
def fund_JZGS_shell(message):
    msg = message.content
    # 返回消息
    return fund_to_shell(msg)


# 基金-账户
@robot.filter(re.compile(".*?login.*?"))
def fund_user_login(message):
    msg = message.content
    return fund_login(msg)


######################【资源分隔】#########################
# 好用不火
@robot.filter('彩蛋')
def learnhybh(message):
    word = '{}/:coffee点击下方蓝色文字查看使用方式\n\n'.format(keyOne) + hybh()
    return word


# hybh2020
@robot.filter('插件下载')
def GetUrlhybh(message):
    path = r"/www/wwwroot/111.229.98.184/app"
    filename = os.listdir(path)[0]
    if ".msi" in filename:
        # fileName = 'allData/keyhybh.txt'
        # with open(fileName, encoding='utf-8') as f:
        #     key = f.read()
        url = "http://111.229.98.184:2020/app/{0}".format(filename)
        return keyWord("Revit插件 " + filename, url, "\n" + url)


# keyworld-MicrosoftEdgeSetup-2020-03-26
@robot.filter('MicrosoftEdge')
def MicrosoftEdgeSetup_app(message):
    return keyWord('MicrosoftEdge下载安装包（此浏览器基于 Chromium 开源项目及其他 开源软件）',
                   'https://pan.baidu.com/s/1I2b9wfvTfacRDycNQR58cA', 'h8s2')


# keyworld-weixin2-2020-03-26
@robot.filter('weixin2')
def weixin2_app(message):
    return keyWord('微信多开工具及源码下载',
                   'https://pan.baidu.com/s/1wCNG195MFLIAAs533V3zrg', 'h0q9')


# keyworld-svp4-2020-03-26
@robot.filter('svp4')
def svp4_app(message):
    return keyWord('svp4插帧软件下载配合potplayer',
                   'https://pan.baidu.com/s/1pSsiVq6CyRN4PquGJS3KZg', '2g5e')


# keyworld-svp4-2020-04-16
@robot.filter('potplayer')
def PotPlayer(message):
    return keyWord('potplayer播放器安装包下载配合svp4',
                   'https://pan.baidu.com/s/19_muL9f_kpS3NZnx9iNEcQ', 'rt1q')


# keyworld-网易云-2019-10-09
@robot.filter('网易云')
def wangYiYun(message):
    return keyWord('网易云灰色歌单资料下载',
                   'https://pan.baidu.com/s/1m1kbYLk3_nU5QGKSgLA--w', 'z5dg')


# keyworld-python-2019-10-09
@robot.filter('python')
def KEYpython(message):
    return keyWord('学习python可以加入这个小组 一起学习',
                   'https://www.yuque.com/groups/pythonlearn/join?token=1h3qPS3e8bv14ZT7')


# keyworld-onedrive-2019-10-09
@robot.filter('oneDrive')
def KEYonedrive(message):
    return keyWord('获取oneDrive 5T网盘账户及使用方式',
                   'https://mp.weixin.qq.com/s/ETl1KknQIaRLqrINdNBHxw')


# keyworld-ppt模板-2019-01-09
@robot.filter('pptx')
def KEYppt(message):
    return keyWord('网络整理3000+ PPT模板百度云下载地址',
                   'https://pan.baidu.com/s/1GWfLR_6RleL-wc_rQ2vN6w', '3ztk')


# keyworld-系统激活-2019-01-09
@robot.filter('系统激活')
def KEYwindows(message):
    return keyWord('管理员运行激活windows系统工具 重装系统也不过期',
                   'https://pan.baidu.com/s/18w7d9ewuHufxlqL6gT8sTw', 'kwmn')


# keyworld-aria2c-2019-01-09
@robot.filter('aria2c')
def KEYaria2c(message):
    return keyWord('Aria2 命令行下载神器，不限速',
                   'https://pan.baidu.com/s/1z7q0xCiHnWVwi34F7XAlEQ', '3cbb')


# keyworld-壁纸-2019-01-09
@robot.filter('壁纸')
def KEYpaper(message):
    return keyWord('无水印超清壁纸百度云下载',
                   'https://pan.baidu.com/s/1bFVG70P4ubbCZYXBXALOVg', 'ehul')


# keyworld-ffmpeg-2019-01-09
@robot.filter('ffmpeg')
def KEYffmpeg(message):
    return keyWord('多媒体视频处理工具FFmpeg有非常强大的功能包括视频采集功能、视频格式转换、视频抓图、给视频加水印等',
                   'https://pan.baidu.com/s/1TPE8JvDdfRxOaswIZJUKJg', '8cjl')


@robot.location
def location_msg(message):
    url = hybh()
    word = '{}/:coffee您发送了一条位置消息\n\n/:coffee点击下方蓝色文字查看使用方式\n'.format(
            keyOne) + url
    return word


@robot.link
def link_msg(message):
    url = hybh()
    word = '{}/:coffee您发送了一条链接消息\n\n/:coffee点击下方蓝色文字查看使用方式\n'.format(
            keyOne) + url
    return word


@robot.voice
def voice_msg(message):
    url = hybh()
    word = '{}/:coffee您发送了一条语音消息\n\n/:coffee点击下方蓝色文字查看使用方式\n'.format(
            keyOne) + url
    return word


# text消息回复
@robot.text
def replayText(message):
    word = '{}/:li还没有相关功能\n/:li确认一下【关键字】【资源】\n/:li点击下方蓝色文字查看使用方式\n\n'.format(
            keyOne) + hybh()
    return word


if __name__ == '__main__':
    robot.run()
