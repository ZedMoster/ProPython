# 回复带链接的消息模板
def keyWord(word=None, url=None, keys=None):
    '''回复带链接的消息模板'''
    if keys == None:
        strWord = '<a href="{0}">{1}</a>'.format(url, word)
    else:
        strWord = '<a href="{0}">{1}</a>\n提取码：{2}'.format(url, word, keys)
    return strWord


# 回复关键词消息模板
def keyStr(word=None):
    strWord = '【{}】\n'.format(word)
    return strWord


# 回复公众号使用方式
def hybh():
    kiss = keyWord('✨好用不火的使用方式', 'https://mp.weixin.qq.com/s/dHP5Q3esmMhPvrPhicOYWQ')
    return kiss


# 在线私有云盘
def pandown():
    start = "✨请点击下方蓝色文字\n\n"
    kiss = start + keyWord('公众号资源分享盘', 'http://haoyongbuhuo.top:88/')
    return kiss


# quark 搜索引擎
def quark(word=None, url=None):
    strWord = '✨点击下方蓝色文字\n\n<a href="{0}">{1}</a>'.format(url, word)
    return strWord


if __name__ == '__main__':
    s1 = keyWord('获取oneDrive 5T网盘账户及使用方式', 'https://mp.weixin.qq.com/s/ETl1KknQIaRLqrINdNBHxw')
    print(s1)
    s2 = keyWord('office2019百度云盘下载地址', 'https://pan.baidu.com/s/1Oi26jZs7jUkqhKqVapkrhg', 'phwa')
    print(s2)
