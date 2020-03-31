#
#   逆转链表，给出头结点地址，以及整数K，每K个元素逆转链表，最后返回结果链表的头结点地址
#
#   样例输入：
#
#   00100 6 4       （头结点 总个数 需要逆转的个数）
#   位置  数据 下一个结点
#   00000 4 99999
#   00100 1 12309
#   68237 6 -1
#   33218 3 00000
#   99999 5 68237
#   12309 2 33218

import math as m
import numpy as np
NULL = -1


class Node(object):
    def __init__(self, address=NULL, element=0, next=NULL):
        self.address = address
        self.element = element
        self.next = next


class LinkedList(object):
    def __init__(self, input):
        self.list = [None] * input[1]
        self.length = input[2]
        node = Node()
        for i in np.arange(3, len(input), 1):
            pos = m.floor((i) / 3) - 1
            remainder = (i) % 3

            if remainder == 0:
                node.address = input[i]
            elif remainder == 1:
                node.element = input[i]
            elif remainder == 2:
                node.next = input[i]
                self.list[pos] = node

                if node.address == input[0]:
                    self.head = node
                    self.headaddress = node.address
                node = Node()

    def GetLength(self):
        return self.length

    def FindElement(self, address):
        for i in self.list:
            if i.address == address:
                return i

    def FindHead(self):
        return self.head

    def PrintAll(self):
        count = 0
        for i in self.list:
            print("address")
            print(i.address)
            print("element")
            print(i.element)
            print("next")
            print(i.next)
            count += 1


def Reverse(L, k):
    cnt = 1
    head = Node(address=NULL, element=0,
                next=L.headaddress)  # 加一个头空结点指向第一个数据结点
    new = L.FindElement(head.next)
    old = L.FindElement(new.next)

    while (cnt < k):
        tmp = L.FindElement(old.next)
        old.next = new.address
        new = old
        old = tmp
        cnt += 1

    L.FindElement(head.next).next = old.address
    return new


if __name__ == "__main__":
    L = LinkedList([
        100, 6, 4, 0, 4, 99999, 100, 1, 12309, 68237, 6, -1, 33218, 3, 0,
        99999, 5, 68237, 12309, 2, 33218
    ])
    L.PrintAll()
    print("---------------reverse---------------")
    Reverse(L, 4)
    L.PrintAll()