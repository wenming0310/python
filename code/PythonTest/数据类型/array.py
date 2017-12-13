'''
scores = []
result_f = open("results.txt")
#name    score
for line in result_f:
    (name,score) = line.split()
    scores.append(float(score))
result_f.close()
print("The top scores were:")
print(scores[0])
print(scores[1])
print(scores[2])
'''
'''
count()     Tells you how many times a value is in the array
extend()    Adds a list of items to an array
index()     Looks for an item and returns its index value
insert()    Adds an item at any index location
pop()       Removes and returns the last array item
remove()    Removes and returns the first array item
reverse()   Reverses the order of the array
sort()      Sorts the array into a specified order(low to high)
'''
#my_array = [7, "24", "Fish", "hat stand", 'A', 1.25]
scores = []
result_f = open("results.txt")
#name    score
for line in result_f:
    (name,score) = line.split()
    scores.append(float(score))
result_f.close()
#scores.sort()       #默认从低到高排序
#scores.reverse()    #将数组反序
scores.sort(reverse=True)
print("The top scores were:")
print(scores[0])
print(scores[1])
print(scores[2])