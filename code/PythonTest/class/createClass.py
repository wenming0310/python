#!/usr/bin/env python
# -*- coding:UTF-8 -*-

class ClassName:
    '类的帮助信息'    #类文档字符串
#     class_suite       #类体
print(ClassName.__doc__)

class Employee:
    '所有员工的基类'
    empCount = 0        #变量是一个类变量，它的值将在这个类的所有实例之间共享，你可以在内部类或外部类使用Employee.empCount访问
    def __init__(self, name, salary):   #第一种__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.name = name                #self代表类的实例，self在定义类的方法时时必须有的，虽然在调用时不必传入相应的参数
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
t = Test()
t.prt()