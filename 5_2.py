
#
# 将一系列给定数字插入一个初始为空的小顶堆H[] 随后对任意给定的下标i，打印从H[i]到根节点的路径
#
#
# 输入样例：
# 5 3
# 46 23 26 24 10
# 5 4 3
#
# 输出样例：
# 24 23 10
# 46 23 10
# 26 10
#

import math as m

NULL = -1
MAXN = 1001
MINH = -10001


class Heap(object):
    def __init__(self, input):
        self.heap = [NULL] * MAXN
        self.length = 0
        self.heap[0] = MINH  # 下标为0处作为哨兵

        for i in input:
            self.Insert(i)

    def Insert(self, node):
        self.length += 1
        i = self.length
        while(self.heap[m.floor(i/2)] > node):
            self.heap[m.floor(i)] = self.heap[m.floor(i/2)]
            i /= 2

        self.heap[m.floor(i)] = node

    def PrintPath(self, pos):
        j = pos
        print(self.heap[j])
        while(j>1):
            j = m.floor(j/2)
            print(self.heap[j])

    def PrintAll(self):
        for i, j in enumerate(self.heap):
            if j > 0:
                print(i)
                print(j)


if __name__ == "__main__":
    H = Heap([46, 23, 26, 24, 10])
    # H.PrintAll()
    H.PrintPath(5)
    print("------")
    H.PrintPath(4)
    print("------")
    H.PrintPath(3)
