# -*- coding=utf-8 -*-
import xlrd
import xlwt
import openpyxl

from datetime import date,datetime

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\\gitee\\YunYouKeJiFeiGongKaiXiangMu\\DataProcess\\1.xls')
    # 获取所有sheet
    print(workbook.sheet_names()) #[u'sheet1', u'sheet2'])
    #sheet1_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    #sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('Sheet1')
    # sheet的名称，行数，列数
    print(sheet1.name,sheet1.nrows,sheet1.ncols)

def write_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\\gitee\\YunYouKeJiFeiGongKaiXiangMu\\DataProcess\\1.xls')
    #workbook1 = xlwt.open_workbook(r'D:\\gitee\\YunYouKeJiFeiGongKaiXiangMu\\DataProcess\\1.xls')  #xlwt用法错误
    sheet1_r = workbook.sheet_by_name('Sheet1')
    #sheet1_w = workbook1.sheet_by_name('Sheet1')
    for i in range(sheet1_r.nrows):
        x = sheet1_r.cell(i, 0).value
        #print(x)
        if x == "heart beat":
            #sheet1_w.write(i,0,label='')
            print(i)

if __name__ == '__main__':
    read_excel()
    write_excel()