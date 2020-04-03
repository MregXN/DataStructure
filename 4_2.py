#
#   给定序列，判断是否能构成同一搜索树
#
#   样例输入：
#   4 2
#   3 1 4 2
#   3 4 1 2
#   3 2 4 1
#   2 1
#   2 1
#   1 2
#   0
#
#   输出样例：
#   YES
#   NO
#   NO

import numpy as np
NULL = -1


class Node(object):
    def __init__(self, element=0, left=NULL, right=NULL, flag=0):
        self.element = element
        self.left = left
        self.right = right
        self.flag = flag


class Tree(object):
    def __init__(self, N, L, input):
        self.length = N
        self.tree = [NULL] * self.length
        for i in np.arange(0, len(input), 1):
            node = Node(input[i], NULL, NULL, 0)
            self.tree[i] = node
            self.InsertNode(self.tree[0], node)
        self.treehead = self.tree[0]

    def InsertNode(self, T, node):
        if T == NULL:
            T = node
        elif node.element < T.element:
            T.left = self.InsertNode(T.left, node)
        elif node.element > T.element:
            T.right = self.InsertNode(T.right, node)

        return T

    def Check(self, T, element):
        if T.flag:
            if element < T.element:
                return self.Check(T.left, element)
            elif element > T.element:
                return self.Check(T.right, element)
            else:
                return 0
        else:
            if element == T.element:
                T.flag = 1
                return 1
            else:
                return 0

    def Judge(self, input):
        if input[0] != self.treehead.element:
            return 0
        else:
            self.treehead.flag = 1

        for i in np.arange(1, len(input), 1):
            if not self.Check(self.treehead, input[i]):
                return 0

        return 1

    def ResetT(self):
        for i in self.tree:
            i.flag = 0

    def PrintAll(self):
        for i in self.tree:
            print("element:")
            print(i.element)

            print("left:")
            if i.left != NULL:
                print(i.left.element)
            else:
                print("NULL")

            print("right:")
            if i.right != NULL:
                print(i.right.element)
            else:
                print("NULL")


if __name__ == "__main__":
    T = Tree(4, 2, [3, 1, 4, 2])

    if T.Judge([3, 4, 1, 2]):
        print("YES")
    else:
        print("NO")

    if T.Judge([3, 2, 4, 1]):
        print("YES")
    else:
        print("NO")

    T.ResetT()

    T = Tree(2, 1, [2, 1])

    if T.Judge([1, 2]):
        print("YES")
    else:
        print("NO")