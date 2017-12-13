#if else
'''
flag = True
if flag:
    print "Welcome to python"
else:
    print "Welcome to php"
'''
#if elif else
'''
score = raw_input("Please input score:")
score = int(score)
if score > 85:
    print "good"
elif 60 <= score <= 85:
    print "pass"
elif 50< score <= 60:
    print "加油"
else:
    print "bad"
'''
#and or
'''
x = int(raw_input("Please input score x:"))
y = int(raw_input("Please input score y:"))

if x > 60 and y > 60:
    print "all pass"
elif x > 60 or y > 60:
    print "one pass"
else:
    print "all fail"
'''
# and or复合使用
'''
year = int(raw_input("Please input the year(e.g.2008):"))

if(year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 ==0):
    print "%d is leap year" %year
else:
    print "%d is not leap year" %year
'''
#for 输出字符串
'''
for i in "abcd":
    print i
'''
#for 输出列表
'''
list = ['Sunday','Monday','Tuesday',
        'Wednesday','Thursday','Friday','Saturday']
for i in list:
    print i
'''
#for 循环输出
'''
for i in [1,1,1,1,1,1]:
    print "hello python"
'''
#for range 从1+到100
'''
sum = 0
for i in range(1,101):#从1加到100
    sum+=i #sum = sum + i
print sum
'''
# for range len
'''
list = ['Sunday','Monday','Tuesday',
        'Wednesday','Thursday','Friday','Saturday']
for i in range(len(list)):
    print list[i]
'''
#for else
#import time 定时模块
'''
import time
for i in range(60):
    print i
    time.sleep(1)
else:
    print "Bye"
'''
#for if复用 pass congtinue break
'''
for i in range(60):
    print i
    if i == 1:
        pass
    if i == 2:
        print "22222"
        continue #跳过循环余下的代码，重新开始下一次循环
    if i == 5:
        break
    print "*"*20
else:
    print "Bye"
for i in range(3):
    print i
'''
#for 冒泡排序
'''
list = [45,13,24,3]
#13,45,24,3
#13,24,45,3
#13,24,3,45

#13,24,3,45
#13,3,24,45

#3,13,24,45

for i in range(1,len(list)):        #同range(0,len(list)-1)
    for j in range(0,len(list)-i):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
        print list
'''
#while循环 1+到100
'''
i = 0
sum = 0
while(i<100):
    i+=1
    sum+=i
print sum
'''
#while if复用
'''
i = ""
while i!="q":
    print "hello pythen"
    i = raw_input("Please input something, q for quit:")
    print i
    if not i:
        break
    if i == "c":
        continue
    print "***********"
else:       #只有在程序正常退出时才会执行else语句（当输入q时）
    print "Bye"
'''

'''
i = 0
while i<10:
    i+=1
    if i%2!=0:
        continue
    elif i>7:
        break
    else:
        print i
'''
#计算器程序，可以完成连续运算
'''
#计算器程序，可以完成连续运算
a = float(raw_input("请输入第一个数字:"))
while 1: 
    b = raw_input("请输入一个运算符：")
    c = float(raw_input("请输入第二个数字:"))
    if b == "+":
        print "result:",a+c
        a=a+c
    elif b == "-":
        print "result:",a-c
        a=a-c
    elif b == "*":
        print "result:",a*c
        a=a*c
    elif b == "/":
        print "result:",a/c
        a=a/c
    else:
        print "Input error. Please input as:+-*/"
        break
'''
#计算器程序，可以完成连续运算
'''
#计算器程序，可以完成连续运算
a = float(raw_input("请输入第一个数字:"))
while 1: 
    b = raw_input("请输入一个运算符：")
    c = float(raw_input("请输入第二个数字:"))
    result = {
        "+":a+c,
        "-":a-c,
        "*":a*c,
        "/":a/c
        }
    a = result.get(b)
    print a
'''
#定义函数
'''
def printstr(str):
    "Print the input string to the standard display device."
    print str
    return
printstr("Welcome to pythoon")
'''
#函数传递
'''
def fun(x):
    print x
fun(1)
#fun(1,2)
'''
#函数传递数组
'''
def pet(x,y):
    print "I want a",x,y
#pet("black","dog")
pet()
'''
#函数定义默认参数
'''
def pet(x="white",y="cat"):
    print "I want a",x,y
#pet("black","dog")
pet()
'''
'''
def pet(x,y="cat"):
    print "I want a",x,y
pet("black","dog")
#pet("white")
'''
#形参传递数字、字符、列表、元组、字典
'''
def f(x):
    print x
f(10)
f("hello")
f([1,2,3])
f((1,2,3))
f({'name':'zz','age':18})
'''
#函数传递双参数
'''
def f(x,y):
    print "My name is %s. I'm %d." %(x,y)

#f('zz',18)
#t=('zz',18)
#f(*t)

t2 = ('zz',18,'female')
f(*t2)
'''
'''
def f(name = "name",city = "city"):
    print "name: %s" % name
    print "city: %s" % city

#f()
#t=('Beijing','zz')
#f(*t)
#d={'name':'zz', 'city':'Beijing'}
#f(name='zz',city='Beijing')
d2={'a':'zz','b':'Beijing'}
#f(**d2)
f(d2['a'],d2['b'])
'''
#函数定义时冗余参数的处理 *arges **kw
'''
def f(x,*args,**kw):
    print x
    print args
    print kw
#f(1,2,3)
#f(x=1)
#f(1)
#f(x=1,y=2)
f(1)
print "*************"
f(1,2,3)
print "*************"
f(x=1)
print "*************"
f(x=1,y=2)
print "*************"
#重复传参f(1,2,3,x=10,y=20,z=30)
f(1,2,3,y=20,z=30)
'''
#函数和return
'''
def fun():
    #return "hello python"
    return range(10)
print fun()
'''
'''
def fun(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    else:
        return 0
    #print "welcome to python"
#fun(1,2)
print fun(2,1)
'''
#return和print的区别
'''
def fun(x,y):
    #print x+y
    return x+y
a=fun(1,2)
print a
'''
#global强制定义全局变量，在函数内定义的全区变量，函数不执行则无效
'''
a=1
def fun():
    a=2
    global b
    b=3
    print a
#fun()
#print fun()
#print a
print b
'''
'''
a=1
def fun():
    global a
    a=2
#fun()
print a
#fun()
#print fun()
#print a
#print b
'''
#lambda
'''
def func(x,y):
    return x*y
print func(2,4)
'''
'''
func=lambda x,y:x*y
print func(2,4)
'''
#reduce 一次对列表内的数进行相加
'''
list = [1,2,3,4]
def add(x,y):
    return x+y
print reduce(add,list)
'''
#reduce lambda 实现1行完成1+到100的程序
#print reduce(lambda x,y:x+y,range(1,101))
#print reduce(lambda x,y:x*y,range(1,5))

#为数字取绝对值
'''
def a(x):
    if(x<0):
        return -x
    return x
print a(-2)
'''
#序列包括字符串、元组、列表
#help(divmod) divmod(7,2) 返回两个数的商和余数
#help(pow) pow(2,3),返回2的3次幂 pow(2,3,5) 2的3次幂然后对5取模
#help(round) round(3.1415926,2) 返回两位小数3.14 round(3.1415926)默认返回一位小数3.1
#callable(f) 判断f是否可调用，是返回True，否返回False
#isinstance(l,list) 判断函数的类型是否复合所给的类型，是返回True，否返回False
#cmp(x,y) 比较两个数的大小，两个数相等返回0，x>y返回1，x<y返回-1
#range(10) 生成0~9的列表list类型
#range(10) 生成0~9的值，每次调用返回一个值，用作循环的话比range好，尤其是返回值很大的时候
#hex(1)返回16进制，oct(1)返回8进制,chr(i) 0<=i<256，返回数字对应的ASCI码字符，ord('a')参数是ASCI码字符，返回的是对应的十进制整数

#str.capitalize(),对字符串进行首字母大写
#s.replace("python","world"),将字符串中的字符替换为给定字符，s.replace("python","world"，2)可选参数2为替换次数控制
'''
s="hello python"
print s.capitalize()
print s.replace("python","world")
s2="123141344154"
'''
#ip.split('.') 将字符以点为分割，分割为字符串，ip.split('.'，1) 可选参数1表示分割次数
'''
ip="192.168.0.1"
ip.split('.')
'''
'''
import string
string.replace(s2,'4','go')
'''
#序列处理函数
#filter(f,range(10))过滤函数
'''
def f(x):
    if x%2==0:
        return True
print filter(f,range(10))
'''
#使用匿名函数取出1~100之间的所有偶数
#print filter(lambda x:x%2==0,range(1,101))
#zip()
#map()
'''
name=["aa","bb","cc"]
age=[15,17,20]
city=["Beijing","Shanghai","Guangzhou"]
print zip(name,age,city)
print map(None,name,age,city)
gender=["male","female"]
print zip(name,age,city,gender)
print map(None,name,age,city,gender)
'''
#add()
'''
a=[1,2,3]
b=[4,5,6]
def add(x,y):
    return x+y
print map(None,a,b)
print map(add,a,b)
print reduce(add,range(1,101))
'''
#交换两个数的值
'''
a=1
b=2
a,b=b,a
a2=3
b2=4
tmp=a2
a2=b2
b2=tmp
'''
#冒泡排序,元组是不可变变量，所以在此要把元组转换为列表
'''
def func(lt=[]):
    if type(lt).__name__!='list' and type(lt).__name__!='tuple':
        return
    if type(lt).__name__=='tuple':
        lt=list(lt)
    if len(lt)<=1:
        return
    else:
        for i in range(1,len(lt)):
            for j in range(len(lt)-i):
                if lt[j]>lt[j+1]:
                    tmp=lt[j]
                    lt[j]=lt[j+1]
                    lt[j+1]=tmp
    return lt
lt=[32,12,3,27,6,9,1]
tp=(2,6,1,9,4)
print func(lt)
print func(tp)
'''
#快速排序
'''
def func(lt=[]):
    if len(lt)<=1:
        return lt
    key=lt[0]
    lt_l=[]
    lt_r=[]
    lt_m=[]

    for i in lt:
        if i<key:
            lt_l.append(i)
            print 'lt_l'
            print lt_l
        elif i>key:
            lt_r.append(i)
            print "lt_r"
            print lt_r
        else:
            lt_m.append(i)
            print "lt_m"
            print lt_m

    lt_l=func(lt_l)
    print "lt_l"
    print lt_l
    lt_r=func(lt_r)
    print "lt_r"
    print lt_r
    return lt_l+lt_m+lt_r

lt=[1,5,12,34,2,5,8,1,9,2,3,4]
#lt=[1,12,5]
print func(lt)
'''
#深拷贝和浅拷贝
#浅拷贝,对引用的拷贝,只拷贝了副对象，所以说id(c)！=id(a)
#对象内部的资源依旧是引用，所以说内部的时候id(c[0])=id(a[0])
#只拷贝了一层,有嵌套的时候呢，修改了嵌套的值原始变量也被修改
'''
a=[0,1,2,3,[4,5,6]]
print a
print id(a)
print id(a[0])
print id(a[4])
print id(a[4][0])
b=a
print b
print id(b)
print id(b[0])
print id(b[4])
print id(b[4][0])

import copy
c=copy.copy(a)
print c
print id(a)
print id(c)
print id(c[0])
print id(c[4])
print id(c[4][0])
print c
c[0] = 9
print c
print a
c[4][0]=44
print c
print a
print id(a)
print id(a[0])
print id(a[4])
print id(a[4][0])
'''
#深拷贝,copy了对象的所有元素，包括嵌套，所以费资源
'''
import copy
a=[0,1,2,3,[4,5,6]]
d=copy.deepcopy(a)
print d
print id(d)
print id(d[0])
print id(d[4])
print id(d[4][0])
'''
#深拷贝 是对对象资源的拷贝,为了保留原始数据，可以在操作之前对原列表进行深拷贝
'''
import copy
def changeme(mylist):
    mylist[0]=18
    print "in:",mylist

mylist=[1,2,3,4,5]
copylist=copy.deepcopy(mylist)
changeme(mylist)
print "out:",copylist
'''
#类
'''
class User(object):
    "User information" #类的描述
#    name='zz'
#    age=18
    count = 0

    def __init__(self,name,age):#构造方法 调用的时候使用初始化函数
        self.name=name
        self.age=age
        User.count+=1
  
    def who(self):
        print "My name is " + self.name + ", I'm "+ str(self.age) + " years old."

    def __del__(self):#销毁的时候执行析构函数
        class_name=self.__class__.__name__
        print class_name,"destroyed"
u1=User('zz',18)
u1.who()
print u1.count

u2=User('aa',20)
u2.who()
print u2.count

print User.__doc__
print User.__name__
print User.__module__
print User.__bases__
print User.__dict__

del u1
'''
#类的继承
'''
class User(object):
    "User information" #类的描述

    def __init__(self,name,age):#调用的时候使用初始化函数
        self.name=name
        self.age=age
  
    def who(self):
        print "My name is " + self.name + ", I'm "+ str(self.age) + " years old."

class Student(User):
    "继承自User类"
    def __init__(self,name,age,height):
        User.__init__(self,name,age)
        self.height=height

    def who(self):
        User.who(self)
        print "My height is " + str(self.height) + "."

Student('zz',18,188).who()
'''
#不允许使用实例化的类访问私有变量
#可使用n._MyCounter__secretCount
'''
class MyCounter(object):
    __secretCount = 0
    publicCount = 0

    def count(self):#定义成员函数
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
        #print self.publicCount

n=MyCounter()#创建一个对象
n.count()#调用成员方法
print n.publicCount
#print n.__secretCount
print n._MyCounter__secretCount
'''
#实例方法
'''
class Test1(object):
    def test1(self):#实例方法
        print "object"

    @classmethod#类方法
    def test2(cls):
        print "class"

    @staticmethod#静态方法
    def test3():
        print "static"
class Test2(Test1):
    @classmethod
    def test2(cls):
        print cls
        print "test2 object"


f1=Test1()
f1.test1()
Test1.test1(f1)
print "----------------"
f1.test2()
Test1.test2()#类方法不需要传递实例的引用
print "----------------"
f1.test3()
Test1.test3()
print "----------------"
Test2.test2()
'''
#try except
'''
try:
    f=open("test.txt","r")
    f.write("This is my file for exception handing.")
except IOError:
    print "Error:can't find file or read data."
else:
    print "Written content in the file sucessfully."
f.close()
print "done"
'''
#try finally
'''
try:
    f=open("test.txt","r")
    f.write("This is my file for exception handing.")
finally:
    print "Error:can't find file or read data."
f.close()
print "done"
'''
#try except try finally 嵌套使用
'''
try:
    f=open("test.txt","r")
    try:
        f.write("This is my file for exception handing.")
    finally:
        print "Going to close the file."
        f.close()
except IOError:
    print "Error:can't find file or read data."
'''
#try except 带参数
'''
try:
    f=open("test.txt","r")
    f.write("This is my file for exception handing.")
except IOError,e:
    print e
    print "Error:can't find file or read data."
else:
    print "Written content in file successfully."
f.close()
print "done"
'''
#raise 出错时给用户一个友好的提示
'''
try:
    #raise Exception("test raise")
    1/0
except Exception,e:
    f=open("error.log","w")
    f.write(str(e)+"\n")
    f.close()
    print e
'''
#时间戳
'''
import time
print time.time()
a=time.localtime()
print a
b=time.localtime(1488891937.18)
print b
print time.mktime(a)
print time.mktime(b)
print time.asctime()
print time.ctime()
print time.strftime('%Y-%m-%d %H:%M:%S')
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-3600))
print time.strptime('2016-01-11 21:12:12','%Y-%m-%d %H:%M:%S')
time.sleep(2)
'''
#实例 输入开始和结束日期，返回连个日期之间的所有日期列表。
'''
import time
def time_list(start,end):
    start1=time.strptime(start,'%Y-%m-%d')
    end1=time.strptime(end,'%Y-%m-%d')
    start2=time.mktime(start1)
    end2=time.mktime(end1)
    res=[]
    while start2<end2:
        tmp=time.strftime('%Y-%m-%d',time.localtime(start2))
        res.append(tmp)
        start2+=86400
    return res
print time_list('2015-1-11','2016-01-11')
'''
#re 模块,写正则匹配时前面通常+r
'''
import re
r=r'ab'
print re.findall(r,'abcdefghigklmnopqrstuvwxyz')
print '\n'
print '\\n'
print r'\n'
#出错f=open("D:\CC++C#Code\python\readme.txt")
f=open(r"D:\CC++C#Code\python\readme.txt")
print f.read()
f.close()
r=r'1\*2'
print re.findall(r,'01*23456701*23')
'''
'''
import re
r=r'^123'
print re.findall(r,'123456123456')
r=r'345$'
print re.findall(r,'12345612345')
r=r'3.5'
print re.findall(r,'123456123456')
r=r'a[a-zA-Z0-9]c'
print re.findall(r,'abc,aCc,a5c,a3c,cfg')
r=r'a[^0-9]c'
print re.findall(r,'abc,aCc,a5c,a3c,cfg')
'''
#正则匹配身份证号,^匹配开头$匹配结尾\d表示数字0到9
'''
import re
r=r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
print re.findall(r,'232303199303101038')
'''
#网页爬虫
'''
import urllib,re,os
content=urllib.urlopen('http://tieba.baidu.com/p/4114581614').read()
#print content
reg=r'src="(http://imgsrc.baidu.com/.+?\.jpg)" >'
imglist=re.findall(reg,content)
x=0
#print imglist
for imgurl in imglist:
    print imgurl
    urllib.urlretrieve(imgurl, 'img'+os.sep+str(x)+'.jpg')
    x+=1
'''
#查看当前python版本支持的文件名,需要提前装载，这里没有提前安装会报错
'''
import pip;
print(pip.pep425tags.get_supported())
'''
'''
import xlrd
'''
#MySQLdb
'''
import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='test1',port=3306,charset='utf8')
cur=conn.cursor()
cur.execute("insert into msg (title,name,content) values ('python','zz','test1 mysql insert')")
conn.commit()
sql="insert into msg (title,name,content) values (%s,%s,%s)"
cur.executemany(sql,[\
    ('test05','zz05','test content05'),\
    ('test06','zz06','test content06'),\
    ])
conn.commit()
import random
sql="insert into user (name,gender) values"
for i in range(100):
    sql+="('user"+str(i)+"',"+str(random.randint(0,1))+"),"
#print sql 
sql=sql[:-1]#切片切掉最后面逗号
#print sql
cur.execute(sql)
conn.commit()
print cur.execute("select * from user")
cur.fetchall()#同时将数据库指针移到最后
cur.scroll(1,mode='absolute')#mode='relative'表示从当前所在行移动到value条mode='absolute'将指针从从结果集的第一行移动value
cur.fetchmany(1)
row=cur.fetchone()
while row:
print row[2]
row=cur.fetchone()

try:
    cur.execute("drop table if exits user")
    conn.commit()
except:
    conn.rollback()
cur.close()
conn.close()
'''
#urllib 网络编程
'''
import urllib
url=r'https://www.sogou.com/'
fp=urllib.urlopen(url)
fp.read()#返回socket信息
fp.info()#返回服务器响应头信息
fp.getcode()#返回200表示请求完成返回404表示网页未找到
fp.geturl()#返回链接
filename=urllib.urlretrieve(url)
type(filename)
print filename#打印临时文件夹路径，服务器响应头信息
filename2=urllib.urlretrieve(url,r'C:\test\sougou.html')
url2=r'http://www.baidu.com/!@#/'
urllib.quote(url2)
urllib.quote_plus(url2)
urllib.unquote(urllib.quote(url2))
urllib.unquote_plus(urllib.unquote(urllib.quote(url2)))
params=urllib.urlencode({'zz':18,'city':'Beijing'})
f=urllib.urlopen("http://python.org/query",params)
f2=urllib.urlopen("http://python.org/query?%s" % params)
f2.read()
'''
#urllib和urllib2的配合使用跳过登录
'''
import urllib,urllib2
import base64
url=r'https://www.baidu.com/'
base64string=base64.encodestring('2469340911@qq.com:Aa123456').strip()#默认删除空白符，此时为删除换行符
authheader="Basic "+base64string
req=urllib2.Request(url)
req.add_header('Authorization',authheader)
urllib2.urlopen(req)
'''
#urlparse
'''
import urllib
import urlparse
url3=r'http://www.baidu.com/user/index.html;20?name=zz&age=18!#8888'
res=urlparse.urlparse(url3)
print res
print res[0]
print res[1]
'''
#phy
from pyh import *
list=[[1,'Lucy',25],[2,'Tom',30],[3,'Lily',20]]
page=PyH('Test')
page<<div(style="text-align:center")<<h4('Test table')
mytab=page<<table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
tr1=mytab<<tr(bgcolor="lightgrey")
tr1<<th('id')+th('name')+th('age')
for i in range(len(list)):
    tr2=mytab<<tr()
    for j in range(3):
        tr2<<td(list[i][j])
        if list[i][j]=="Tom":
            tr2.attributes['bgcolor']='yellow'
        if list[i][j]=="Lily":
            tr2[1].attributes['style']='color:red'
page.printOut('test.html')
