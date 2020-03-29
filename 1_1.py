#
#   给定N个整数的序列，求最大连续子列和，当和为负数时则返回零
#

import numpy as np
import math


# 算法1
def MaxSubseqSum1(A, N):
    MaxSum = 0
    for i in np.arange(0, N, 1):
        for j in np.arange(0, N, 1):
            ThisSum = 0
            for k in np.arange(i, j, 1):
                ThisSum += A[k]
            if ThisSum > MaxSum:
                MaxSum = ThisSum

    return MaxSum


# 算法2
def MaxSubseqSum2(A, N):
    MaxSum = 0
    for i in np.arange(0, N, 1):
        ThisSum = 0
        for j in np.arange(0, N, 1):
            ThisSum += A[j]
            if ThisSum > MaxSum:
                MaxSum = ThisSum

    return MaxSum


# 算法3
def MaxSubseqSum3(A, left, right):
    if left == right:
        return A[left]

    mid = (left + right) / 2
    MaxLeftSum = MaxSubseqSum3(A, left, math.floor(mid))
    MaxRightSum = MaxSubseqSum3(A, math.ceil(mid), right)

    MaxLeftBorderSum = 0
    LeftBorderSum = 0
    for i in np.arange(math.floor(mid), left - 1, -1):
        LeftBorderSum += A[i]
        if LeftBorderSum > MaxLeftBorderSum:
            MaxLeftBorderSum = LeftBorderSum

    MaxRightBorderSum = 0
    RightBorderSum = 0
    for i in np.arange(math.ceil(mid), right + 1, 1):
        RightBorderSum += A[i]
        if RightBorderSum > MaxRightBorderSum:
            MaxRightBorderSum = RightBorderSum
    return max(MaxLeftSum, MaxRightSum, MaxLeftBorderSum + MaxRightBorderSum)


# 算法4
def MaxSubseqSum4(A, N):
    ThisSum = 0
    MaxSum = 0

    for i in A:
        ThisSum += i
        if ThisSum > MaxSum:
            MaxSum = ThisSum
        elif ThisSum < 0:
            ThisSum = 0

    return MaxSum


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, -6, 7, -8]
    result1 = MaxSubseqSum1(A, len(A))
    result2 = MaxSubseqSum2(A, len(A))
    result3 = MaxSubseqSum3(A, 0, len(A) - 1)
    result4 = MaxSubseqSum4(A, len(A))

    print(result1)
    print(result2)
    print(result3)
    print(result4)