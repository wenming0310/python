#-*- coding:utf-8 -*-
import unittest
from  randomyear import getrandomyear,leapyeartestcase
from 计算闰年 import *

class LeapYearTestClass(unittest.TestCase):
    "测试计算闰年"
    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formmed_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
