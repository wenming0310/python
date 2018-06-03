#-*- coding:utf-8 -*-
import random

def getrandomyear(quantity):
    a = []
    for i in range(quantity):
        a.append(random.randint(0, 10000))
    return a

leapyeartestcase = [1700, 1800, 1900, 2000, 2004, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2100, 2200, 2300, 2400]

if __name__ == '__main__':
    print(getrandomyear(10))
    print(leapyeartestcase)