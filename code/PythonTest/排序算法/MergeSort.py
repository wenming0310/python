'''
#归并排序，算法导论伪代码
#A是一个数组，p、q和r是数组下标，满足p≤q<r，该过程假设子数组A[p..q]和A[q+1..r]都已排序好
#合并这两个子数组形成单一的已排序好的字数度并代替当前的子数组A[p..r]
MERGE(A, p, q, r)
n1 = q - p + 1
n2 = r - q
let L[1..n1+1] and R[1..n2+1] be new arrays
for i = 1 to n1
    L[i] = A[p + i - 1]
for j = 1 to n2
    R[j] = A[q + j]
L[n1 + 1] = ∞
R[n2 + 1] = ∞
i = 1
j = 1
for k = p to r
    if L[i]≤R[j]
        A[k] = L[i]
        i = i + 1
    else A[k] = R[j]
        j = j + 1
'''
