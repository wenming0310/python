'''
Array                       A variable with multiple indexed slots for holding data
linked list                 A variable that creates a chain of data where one data item points to another data item,which itself points to another data item, and another, and so on and so forth
Queue                       A variable that allows data to enter at one end of a collection and leave at the other end,supporting a first-in, first-out mechanism
Hash                        A variable that has exactly two columns and (potentially) many rows of data
Set                         A variable that contains a collection of unique data items
Multi-dimensional array     A variable that contains data arranged as a matrix of multiple dimensions (but typically, only two)
'''
'''
scores = [] #定义数组
names = []
result_f = open("results.txt")
for line in result_f:
    (name,score) = line.split()
    scores.append(float(score)) #数组赋值
    names.append(name)
result_f.close()
scores.sort()   #排序方法（由小到大）
scores.reverse()    #数据反向（将原排列顺序颠倒）
names.sort()
names.reverse()
print("The highest scores were: ")
print(names[0] + ' with ' + str(scores[0]))
print(names[1] + ' with ' + str(scores[1]))
print(names[2] + ' with ' + str(scores[2]))
'''
'''
scores = {}     #curly bracket波形括号表示定义的是Hash(Dictionary)([]表示数组) key在前，值在后{1:2,2:3,3:4}
scores[8.45] = 'Joseph'
scores[9.12] = 'Juan'
scores[7.21] = 'Zack'

for key in scores.keys():
    print(scores[key] + ' had a score of ' + str(key))

for score,surfer in scores.items():
    print(surfer + ' had a score of ' + str(score))
'''
'''
scores = {} #创建字典
result_f = open("results.txt")  #打开文件
for line in result_f:
    (name,score) = line.split() #分割行
    scores[score] = name        #给字典赋值，以score为键
result_f.close()    #关闭文件
print("The highest scores were: ")
#for each_score in scores.keys():
#    print('Surfer ' + scores[each_score] + ' scored ' + each_score)
for each_score in sorted(scores.keys(), reverse = True):            #hash 字典没有.sort方法，可以直接使用sorted（）函数
    print('Surfer ' + scores[each_score] + ' scored ' + each_score)
'''
'''
line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"
s = {}
(s['ID'],s['Name'],s['Country'],s['Average'],s['BoardType'],s['Age']) = line.split(';') #以";"分割行
print("ID:          " + s['ID'])
print("Name:        " + s['Name'])
print("Country:     " + s['Country'])
print("Average:     " + s['Average'])
print("Board Type:  " + s['BoardType'])
print("Age:         " + s["Age"])
'''
def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for each_line in surfers_f:
        s = {}  #创建dict（字典）类型数据
        (s['ID'], s['Name'], s['Country'], s['Average'], s['BoardType'], s['Age']) = each_line.split(';')  # 分割行
        if id2find == int(s['ID']):
            surfers_f.close()
            return s
    surfers_f.close()
    return {}   #返回dict类型
lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID:          " + surfer['ID'])
    print("Name:        " + surfer['Name'])
    print("Country:     " + surfer['Country'])
    print("Average:     " + surfer['Average'])
    print("Board Type:  " + surfer['BoardType'])
    print("Age:         " + surfer["Age"])
print(type(surfer))
print(type(int))