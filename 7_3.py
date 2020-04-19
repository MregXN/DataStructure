#
# 完全二叉搜索树
#
#  输入： 1 2 3 4 5 6 7 8 9 0
#  输出：（完全二叉树的层序遍历） 6 3 8 1 5 7 9 0 2 4

import math as m

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
T = [-1] * 10


def GetLeftLength(n):
    H = m.floor(m.log(n+1, 2))
    X = n + 1 - 2**H

    if X > 2**(H - 1):
        X = 2**(H - 1)

    return 2**(H - 1) - 1 + X


def solve(ALeft, ARight,
          TRoot):  # ALeft要考虑的最左边元素的下标 ARight要考虑的最右边的下标  TRoot结果数组内所考虑的节点位置
    # 初始调用为 0， N-1 ，0
    n = ARight-ALeft + 1
    if (n == 0):
        return
    L = GetLeftLength(n)
    T[TRoot] = A[int(ALeft + L)]
    LeftTRoot = 2 * TRoot + 1
    RightTRoot = LeftTRoot + 1
    solve(ALeft, ALeft + L - 1, LeftTRoot)
    solve(ALeft + L + 1, ARight, RightTRoot)


if __name__ == "__main__":
    solve(0, 9, 0)
    print(T)