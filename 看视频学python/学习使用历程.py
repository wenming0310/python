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
    print "����"
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
# and or����ʹ��
'''
year = int(raw_input("Please input the year(e.g.2008):"))

if(year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 ==0):
    print "%d is leap year" %year
else:
    print "%d is not leap year" %year
'''
#for ����ַ���
'''
for i in "abcd":
    print i
'''
#for ����б�
'''
list = ['Sunday','Monday','Tuesday',
        'Wednesday','Thursday','Friday','Saturday']
for i in list:
    print i
'''
#for ѭ�����
'''
for i in [1,1,1,1,1,1]:
    print "hello python"
'''
#for range ��1+��100
'''
sum = 0
for i in range(1,101):#��1�ӵ�100
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
#import time ��ʱģ��
'''
import time
for i in range(60):
    print i
    time.sleep(1)
else:
    print "Bye"
'''
#for if���� pass congtinue break
'''
for i in range(60):
    print i
    if i == 1:
        pass
    if i == 2:
        print "22222"
        continue #����ѭ�����µĴ��룬���¿�ʼ��һ��ѭ��
    if i == 5:
        break
    print "*"*20
else:
    print "Bye"
for i in range(3):
    print i
'''
#for ð������
'''
list = [45,13,24,3]
#13,45,24,3
#13,24,45,3
#13,24,3,45

#13,24,3,45
#13,3,24,45

#3,13,24,45

for i in range(1,len(list)):        #ͬrange(0,len(list)-1)
    for j in range(0,len(list)-i):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
        print list
'''
#whileѭ�� 1+��100
'''
i = 0
sum = 0
while(i<100):
    i+=1
    sum+=i
print sum
'''
#while if����
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
else:       #ֻ���ڳ��������˳�ʱ�Ż�ִ��else��䣨������qʱ��
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
#���������򣬿��������������
'''
#���������򣬿��������������
a = float(raw_input("�������һ������:"))
while 1: 
    b = raw_input("������һ���������")
    c = float(raw_input("������ڶ�������:"))
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
#���������򣬿��������������
'''
#���������򣬿��������������
a = float(raw_input("�������һ������:"))
while 1: 
    b = raw_input("������һ���������")
    c = float(raw_input("������ڶ�������:"))
    result = {
        "+":a+c,
        "-":a-c,
        "*":a*c,
        "/":a/c
        }
    a = result.get(b)
    print a
'''
#���庯��
'''
def printstr(str):
    "Print the input string to the standard display device."
    print str
    return
printstr("Welcome to pythoon")
'''
#��������
'''
def fun(x):
    print x
fun(1)
#fun(1,2)
'''
#������������
'''
def pet(x,y):
    print "I want a",x,y
#pet("black","dog")
pet()
'''
#��������Ĭ�ϲ���
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
#�βδ������֡��ַ����б�Ԫ�顢�ֵ�
'''
def f(x):
    print x
f(10)
f("hello")
f([1,2,3])
f((1,2,3))
f({'name':'zz','age':18})
'''
#��������˫����
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
#��������ʱ��������Ĵ��� *arges **kw
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
#�ظ�����f(1,2,3,x=10,y=20,z=30)
f(1,2,3,y=20,z=30)
'''
#������return
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
#return��print������
'''
def fun(x,y):
    #print x+y
    return x+y
a=fun(1,2)
print a
'''
#globalǿ�ƶ���ȫ�ֱ������ں����ڶ����ȫ��������������ִ������Ч
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
#reduce һ�ζ��б��ڵ����������
'''
list = [1,2,3,4]
def add(x,y):
    return x+y
print reduce(add,list)
'''
#reduce lambda ʵ��1�����1+��100�ĳ���
#print reduce(lambda x,y:x+y,range(1,101))
#print reduce(lambda x,y:x*y,range(1,5))

#Ϊ����ȡ����ֵ
'''
def a(x):
    if(x<0):
        return -x
    return x
print a(-2)
'''
#���а����ַ�����Ԫ�顢�б�
#help(divmod) divmod(7,2) �������������̺�����
#help(pow) pow(2,3),����2��3���� pow(2,3,5) 2��3����Ȼ���5ȡģ
#help(round) round(3.1415926,2) ������λС��3.14 round(3.1415926)Ĭ�Ϸ���һλС��3.1
#callable(f) �ж�f�Ƿ�ɵ��ã��Ƿ���True���񷵻�False
#isinstance(l,list) �жϺ����������Ƿ񸴺����������ͣ��Ƿ���True���񷵻�False
#cmp(x,y) �Ƚ��������Ĵ�С����������ȷ���0��x>y����1��x<y����-1
#range(10) ����0~9���б�list����
#range(10) ����0~9��ֵ��ÿ�ε��÷���һ��ֵ������ѭ���Ļ���range�ã������Ƿ���ֵ�ܴ��ʱ��
#hex(1)����16���ƣ�oct(1)����8����,chr(i) 0<=i<256���������ֶ�Ӧ��ASCI���ַ���ord('a')������ASCI���ַ������ص��Ƕ�Ӧ��ʮ��������

#str.capitalize(),���ַ�����������ĸ��д
#s.replace("python","world"),���ַ����е��ַ��滻Ϊ�����ַ���s.replace("python","world"��2)��ѡ����2Ϊ�滻��������
'''
s="hello python"
print s.capitalize()
print s.replace("python","world")
s2="123141344154"
'''
#ip.split('.') ���ַ��Ե�Ϊ�ָ�ָ�Ϊ�ַ�����ip.split('.'��1) ��ѡ����1��ʾ�ָ����
'''
ip="192.168.0.1"
ip.split('.')
'''
'''
import string
string.replace(s2,'4','go')
'''
#���д�����
#filter(f,range(10))���˺���
'''
def f(x):
    if x%2==0:
        return True
print filter(f,range(10))
'''
#ʹ����������ȡ��1~100֮�������ż��
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
#������������ֵ
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
#ð������,Ԫ���ǲ��ɱ�����������ڴ�Ҫ��Ԫ��ת��Ϊ�б�
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
#��������
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
#�����ǳ����
#ǳ����,�����õĿ���,ֻ�����˸���������˵id(c)��=id(a)
#�����ڲ�����Դ���������ã�����˵�ڲ���ʱ��id(c[0])=id(a[0])
#ֻ������һ��,��Ƕ�׵�ʱ���أ��޸���Ƕ�׵�ֵԭʼ����Ҳ���޸�
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
#���,copy�˶��������Ԫ�أ�����Ƕ�ף����Է���Դ
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
#��� �ǶԶ�����Դ�Ŀ���,Ϊ�˱���ԭʼ���ݣ������ڲ���֮ǰ��ԭ�б�������
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
#��
'''
class User(object):
    "User information" #�������
#    name='zz'
#    age=18
    count = 0

    def __init__(self,name,age):#���췽�� ���õ�ʱ��ʹ�ó�ʼ������
        self.name=name
        self.age=age
        User.count+=1
  
    def who(self):
        print "My name is " + self.name + ", I'm "+ str(self.age) + " years old."

    def __del__(self):#���ٵ�ʱ��ִ����������
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
#��ļ̳�
'''
class User(object):
    "User information" #�������

    def __init__(self,name,age):#���õ�ʱ��ʹ�ó�ʼ������
        self.name=name
        self.age=age
  
    def who(self):
        print "My name is " + self.name + ", I'm "+ str(self.age) + " years old."

class Student(User):
    "�̳���User��"
    def __init__(self,name,age,height):
        User.__init__(self,name,age)
        self.height=height

    def who(self):
        User.who(self)
        print "My height is " + str(self.height) + "."

Student('zz',18,188).who()
'''
#������ʹ��ʵ�����������˽�б���
#��ʹ��n._MyCounter__secretCount
'''
class MyCounter(object):
    __secretCount = 0
    publicCount = 0

    def count(self):#�����Ա����
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount
        #print self.publicCount

n=MyCounter()#����һ������
n.count()#���ó�Ա����
print n.publicCount
#print n.__secretCount
print n._MyCounter__secretCount
'''
#ʵ������
'''
class Test1(object):
    def test1(self):#ʵ������
        print "object"

    @classmethod#�෽��
    def test2(cls):
        print "class"

    @staticmethod#��̬����
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
Test1.test2()#�෽������Ҫ����ʵ��������
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
#try except try finally Ƕ��ʹ��
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
#try except ������
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
#raise ����ʱ���û�һ���Ѻõ���ʾ
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
#ʱ���
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
#ʵ�� ���뿪ʼ�ͽ������ڣ�������������֮������������б�
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
#re ģ��,д����ƥ��ʱǰ��ͨ��+r
'''
import re
r=r'ab'
print re.findall(r,'abcdefghigklmnopqrstuvwxyz')
print '\n'
print '\\n'
print r'\n'
#����f=open("D:\CC++C#Code\python\readme.txt")
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
#����ƥ�����֤��,^ƥ�俪ͷ$ƥ���β\d��ʾ����0��9
'''
import re
r=r'^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$'
print re.findall(r,'232303199303101038')
'''
#��ҳ����
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
#�鿴��ǰpython�汾֧�ֵ��ļ���,��Ҫ��ǰװ�أ�����û����ǰ��װ�ᱨ��
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
sql=sql[:-1]#��Ƭ�е�����涺��
#print sql
cur.execute(sql)
conn.commit()
print cur.execute("select * from user")
cur.fetchall()#ͬʱ�����ݿ�ָ���Ƶ����
cur.scroll(1,mode='absolute')#mode='relative'��ʾ�ӵ�ǰ�������ƶ���value��mode='absolute'��ָ��Ӵӽ�����ĵ�һ���ƶ�value
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
#urllib ������
'''
import urllib
url=r'https://www.sogou.com/'
fp=urllib.urlopen(url)
fp.read()#����socket��Ϣ
fp.info()#���ط�������Ӧͷ��Ϣ
fp.getcode()#����200��ʾ������ɷ���404��ʾ��ҳδ�ҵ�
fp.geturl()#��������
filename=urllib.urlretrieve(url)
type(filename)
print filename#��ӡ��ʱ�ļ���·������������Ӧͷ��Ϣ
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
#urllib��urllib2�����ʹ��������¼
'''
import urllib,urllib2
import base64
url=r'https://www.baidu.com/'
base64string=base64.encodestring('2469340911@qq.com:Aa123456').strip()#Ĭ��ɾ���հ׷�����ʱΪɾ�����з�
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
