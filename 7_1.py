# 检查是否是哈夫曼编码：
#     1.最优编码： 总长度（WPL）最小
#     2.无歧义解码： （前缀码），数据仅存于叶子结点
#     3.没有度为1的结点：  满足1,2一定满足3

import math as m
import numpy as np

NULL = -1
MAXN = 1001
MINH = -10001


class TreeNode(object):
    def __init__(self, weight=0, left=NULL, right=NULL):
        self.weight = weight
        self.left = left
        self.right = right


class Heap(object):
    def __init__(self, input):
        min = TreeNode(MINH)
        self.heap = [NULL] * MAXN
        self.length = 0
        self.heap[0] = min  # 下标为0处作为哨兵

        for i in input:
            t = TreeNode(i)
            self.Insert(t)

    def Insert(self, node):
        self.length += 1
        i = self.length
        while (self.heap[m.floor(i / 2)].weight > node.weight):
            self.heap[m.floor(i)] = self.heap[m.floor(i / 2)]
            i /= 2

        self.heap[m.floor(i)] = node

    def DeleteMin(self):
        self.length -= 1
        i = self.length
        return self.heap[i]

    def PrintAll(self):
        for i in np.arange(1, self.length+1, 1):
            # if type(i).__name__ == 'TreeNode':
            print(self.heap[i].weight)


def Huffman(input):
    T = TreeNode()
    H = Heap(input)
    for i in np.arange(1,H.length+1,1):
        T.left = H.DeleteMin()
        T.right = H.DeleteMin()
        T.weight = T.left.weight + T.right.weight
        H.Insert(T)
    T = H.DeleteMin()

    H.PrintAll()
    return T


if __name__ == '__main__':
    H = Huffman([1, 2, 3, 4])
