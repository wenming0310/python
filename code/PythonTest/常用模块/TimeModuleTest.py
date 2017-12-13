import time

#a = time.clock()   #不同系统含义不同，nuix返回进程时间（用秒表示的浮点数（时间戳））；windows第一次调用返回进程的实际时间，第二次之后返回的是自第一次调用至再次调用的间隔时间（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
#time.daylight()    #返回的数据类型不知道
#a = time.gmtime()   #将时间戳转换为UTC时区（0时区）的struct_time，time.gmtime(1505294759.5496376)，若未提供返回当前时间戳
#a = time.localtime()    #将一个时间戳转换为当前时区的struct_time，若未提供自已当前时间为准time.localtime(1505294759.5496376)
#time.sleep(5)  #睡眠 s为单位
#a = time.time() #返回当前时间戳
#a = time.mktime(time.gmtime(1505294759.5496376))   #将struct_time转化为时间戳，精度下降了
#a = time.asctime()   #把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。如果没有参数，将会将time.localtime()作为参数传入
#a = time.ctime()  #把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
#a = time.strftime("%Y-%m-%d %X", time.localtime())  #把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
#a = time.timezone()    #不知道参数是什么
a = time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X') #time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')

print(a)
print("Wake!")
