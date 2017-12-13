import re
def isnumber(num):
    regex = re.compile(r"^(-?\d+)(\.\d*)?$")
    if re.match(regex,num):
        return True
    else:
        return False

def is_float(s):
    s = str(s)   # 强制转化操作是因为传进来的被判断对象的类型具有不确定性，你需要将其统一在一个起点进行处理。
    if s.count('.') == 1:  # 小数的首要前提就是有且只有一个小数点。
        s_left = s.split('.')[0]  # 以小数点为分界点把字符串拆成左右两部分以备进一步分析。
        s_right = s.split('.')[1]
        if s_left.isdigit() and s_right.isdigit(): # 小数点左右都是纯的正整数，一个标准的正小数情况。
            return True
        elif s_left.startswith('-')and s_left.count('-') == 1 and s_right.isdigit():
            # 负小数情况稍复杂，首先以负号开头，排除多个负号情况，同时小数点右侧是纯的正整数，在此情况下，
            if s_left.split('-')[1].isdigit():  # 小数点左侧负号身后的部分如果是正整数字符，是个合法的负小数
                return True
    return False
    # 除了以上正小数和负小数两种合法的情况外，其它均是不合法情况，上边的判断路线也走不进去，直接返回False结束。
    # 而当符合上面的任何条件都会判断是合法小数，返回True结束程序，也走不到最后的return False这个语句。
    # 所以不用看到程序最后一句是 return False 而担心。
while 1:
    a = input()
    print('isnumber',isnumber(a))
    print('is_float',is_float(a))