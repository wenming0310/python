#! /user/bin/env python #第一行是特殊注释行，称之为组织行，用来告诉我们GUN/Linux系统应该使用哪个解释器来执行该程序
# -*- coding:utf-8 -*-
# FileName : pic.py
# Auther : Eric
# Date: 2017年12月15日22:11:40

import re # 导入正则表达式模块，提取网页中所需要的内容
import requests # python HTTP客户端，编写爬虫和测试服务器响应数据经常会用到的
import random   # 随机生成一个实数，他的范围[0,1]内

def spiderPic(html, keyword):
    print('正在查找：' + keyword + '对应的图像，正在从百度图片中下载文件，请稍等...')
    for addr in re.findall('"objURL":".*?"', html, re.s):
        print('现在正在爬取URL地址：' + str(addr)[0:30] + "...")
        try:
            pics = requests.get(addr, timeout=10) # 请求URL地址（最大时间10s）
        except requests.exceptions.ConnectionError:
            print('您当前的URL地址请求错误！')
            continue
        fq = open('E:\\pic\\' + (keyword + '_' +  str(random.randrange(0,1000,4))) + '.jpg')
        fq.write(pics.content)
        fq.close()


# python 的主方法
if __name__ == '__main__':
    word = input('请输入你想要爬取的图像的关键词：')
    requests = requests.get('https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111' +  spiderPic('', word))
# 调用函数

spiderPic('', word)