#  画地图
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
# 定义人所在的位置（初始化）
x = 2
y = 1
endx = 7
endy = 9
# 用字符串重新给地图赋值
def print_map():
    for nums in map_data:
        for num in nums:
            if num == 1:
                print(" #",end=" ")
            elif(num == 0):
                print("  ",end=" ")
            else:
                print(" $",end=" ")
        print("")

# 所用到的核心知识

# print("交换前的地图")
# print_map()
# map_data[2][1], map_data[2+1][1] = map_data[2+1][1], map_data[2][1]
# print("交换后的地图")
# print_map()

# 先画地图
print_map()
while True:
#  指令的输入
    order = input("请输入指令（a: 左，s: 下， d: 右, w: 上）：")
# 对用户输入的指令进行判断
    # 当用户输入a时执行向左走进行交换（列变行不变 列下标减1）
    if order == "a":
        y = y-1
        # 碰到墙，游戏结束
        if map_data[x][y] == 1:
            print("游戏结束")
            break
        else:
            map_data[x][y],map_data[x][y+1] = map_data[x][y+1], map_data[x][y]  # 进行交换操作
            print_map()

    # 当用户输入s时执行向下走进行交换（列不变行变 行下标加1）
    elif order == "s":
        x = x + 1
        if map_data[x][y] == 1:
            print("游戏结束")
            break
        else:
            map_data[x][y], map_data[x-1][y] = map_data[x-1][y], map_data[x][y]  # 进行交换操作
            print_map()

    # 当用户输入d时执行向右走进行交换（列变行不变 列下标加1）
    elif order == "d":
        y = y + 1
        if map_data[x][y] == 1:
            print("游戏结束")
            break
        else:
            map_data[x][y], map_data[x][y - 1] = map_data[x][y - 1], map_data[x][y]  # 进行交换操作
            print_map()
            if map_data[x][y] == map_data[endx][endy]:
                print("恭喜你过关了")
                break

    # 当用户输入w时执行向上走进行交换（列不变行变 行下标减1）
    elif order == "w":
        x = x - 1
        if map_data[x][y] == 1:
            print("游戏结束")
            break
        else:
            map_data[x][y], map_data[x + 1][y] = map_data[x + 1][y], map_data[x][y]  # 进行交换操作
            print_map()

    # 当用户输入非规则内的指令时的错误提示，并重新输入
    else:
        print("您输入指令有误，请重新按指令规则输入！")
        continue