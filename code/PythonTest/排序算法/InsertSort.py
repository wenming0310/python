'''
#插入排序算法导论伪代码
j=2
for j in range(len(A)):
    key = A[j]
    i = j - 1
    while i>0 and A[i]>key:
        A[i+1] = A[i]
         i = i - 1
    A[i+1] = key
'''

#插入排序，从小到大
def InsertForwardSort(localityArray):
    for j in range(1,len(localityArray)):
        #print(j)
        key = localityArray[j]
        index = j
        while index > 0 and localityArray[index-1] > key:
            localityArray[index] = localityArray[index-1]
            index = index - 1
        localityArray[index] = key

##插入排序，从大到小
def InsertBackwardSort(localityArray):
    for j in range(1,len(localityArray)):
        #print(j)
        key = localityArray[j]
        index = j
        while index > 0 and localityArray[index-1] < key:
            localityArray[index] = localityArray[index-1]
            index = index - 1
        localityArray[index] = key

array = [31,41,59,26,41,58]
InsertForwardSort(array)
print(array)
InsertBackwardSort(array)
print(array)