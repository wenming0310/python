#-*- coding:utf-8 -*-
'''
#导入模块
from PIL import Image
#读取文件
img = Image.open('test.jpg')
#保存文件
#img.save(filename,format)
img.save(filename,"JPEG")
img_mode = img.mode
#图片模式的转换
img = img.convert("L")  #转化成灰度图像
#获取每个坐标的像素点的RGB值
r,g,b = img.getpixel((j,i))
#重设图片大小
img = img.resize(width,height)
#创建缩略图
img.thumbnail(size)

#获取图片大小
(width,height) = img.size
#获取图片的源格式
img_format = img.format
#获取图片模式，有三种模式：L(灰度图像)，RGB(真彩色)和CMYK(pre-press图像)

#链接：https://www.jianshu.com/p/3af5e7ce1d58
'''
from PIL import Image
#要索引的字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)
img = Image.open('小猪佩奇.jpg')      #读取图像文件
(width,height) = img.size
img = img.resize((int(width*0.5),int(height*0.2)))  #对图像进行一定缩小,图片的大小可以根据上传图片的大小来按需调节，
print(img.size)
def convert(img):
    img = img.convert("L")  # 转为灰度图像
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))     # 获取每个坐标像素点的灰度
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)] #获取对应坐标的字符值
        txt += '\n'
    return  txt

def convert1(img):
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            r,g,b = img.getpixel((j, i))           #获取每个坐标像素点的rgb值
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)   #通过灰度转换公式获取灰度
            unit = (256.0+1)/length
            txt += ascii_char[int(gray / unit)]  # 获取对应坐标的字符值
        txt += '\n'
    return txt

txt = convert(img)
f = open("03_convert.txt","w")
f.write(txt)            #存储到文件中
f.close()
