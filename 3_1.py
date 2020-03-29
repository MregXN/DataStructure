#
#   给定两棵树，判断是否同构
#
#
#   输入样例： 8 A12 B34 C5- D-- E6- G7- F-- H--
#             8 G-4 B76 F-- A51 H-- C0- D-- E2-
#
#   ps: 同构指两棵子树T1和T2，如果T1可以通过若干次左右孩子互换变成T2，则我们称两棵树是同构的
#
#   利用结构数组表示二叉树： 静态链表，左右儿子用数组下标表示，不存在用-表示
# 
import math as m
import numpy as np
NULL = "-"


class Node(object):
    def __init__(self, element=0, left=0, right=0):
        self.element = element
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, input):
        self.tree = [None]*input[0]
        node = Node()
        for i in np.arange(1, len(input), 1): 
            pos = m.floor((i - 1) / 3)
            remainder = (i - 1) % 3

            if remainder == 0:
                node.element = input[i]
            elif remainder == 1:
                node.left = input[i]
            elif remainder == 2:
                node.right = input[i]
                self.tree[pos] = node
                node = Node()

    def PrintAll(self):
        count = 0
        for i in self.tree:
            count += 1
            print("element" + str(count))
            print(i.element)
            print("left")
            print(i.left)
            print("right")
            print(i.right)

    def FindRoot(self):
        check = [0]*len(self.tree)
        for i in self.tree:
            if i.left != NULL:
                check[i.left] =1;
            if i.right != NULL:
                check[i.right] =1;           

        for i in np.arange(0, len(check), 1): 
            if check[i] != 1:
                self.Root = self.tree[i].element
        return self.Root

if __name__ == "__main__":
    input1 = [
        8, "A", 1, 2, "B", 3, 4, "C", 5, "-", "D", "-", "-", "E", 6, "-", "G",
        7, "-", "F", "-", "-", "H", "-", "-"
    ]
    input2 = [
        8, "G", "-", 4, "B", 7, 6, "F", "-", "-", "A", 5, 1, "H", "-", "-",
        "C", 0, "-", "D", "-", "-", "E", 2, "-"
    ]

    T1 = Tree(input1)
    T2 = Tree(input2)
    print(T1.FindRoot())
    print(T2.FindRoot())