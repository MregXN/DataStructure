# 给定N个数字的排列，如何仅利用与0交换达到排序的目的？

# 下标 0 1 2 3 4 5 6 7 8 9
# 元素 3 5 7 2 6 4 9 0 8 1
# 指针 7 9 3 0 5 1 4 2 8 6 

import numpy as np

A = [3, 5, 7, 2, 6, 4, 9, 0, 8, 1]
T = [7, 9, 3, 0, 5, 1, 4, 2, 8, 6]



if __name__ == "__main__":
    time = 0
    for i in np.arange(0,len(A),1):
        if (T[i] == i):
            continue
        else:
            pos = i
            temp = A[pos]
            while(A[T[pos]] != T[pos]):
                A[pos]= A[T[pos]]
                pos_temp = T[pos]
                T[pos] = pos
                pos = pos_temp
                time +=1
            
            A[pos] = temp
            T[pos] = pos
            time +=1

    print(A)
    print(T)
    print("count : %d"%time)