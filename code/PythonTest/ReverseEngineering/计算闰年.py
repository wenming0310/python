# -*- coding=utf-8 -*-
# 计算今年是否是闰年。判断闰年条件，满足年份模 400 为 0，或者模 4 为 0 但模 100 不为 0。

inputnum = int(input("请输入年（例2018）："))

if inputnum is None:
    print("输入格式错误！")
    exit()
resaulta = inputnum % 400

resault1 = inputnum % 4
resault2 = inputnum % 100
resaultb = 2
if resault1 == 0:
    if resault2 != 0:
        resaultb = 0
    else:
        resaultb = 2
else:
    resaultb = 2


if (resaulta == 0) or (resaultb == 0):
    print("该年是闰年！")
else:
    print("该年不是闰年！")
