#
# 利用邻接表表示图: 邻接表，G[N]为指针数组，对应矩阵每行一个链表，只存非0元素
#

import numpy as np
NULL = -1


class GNode(object):
    def __init__(self, Nv, Ne):
        self.Nv = Nv
        self.Ne = Ne 
        self.G = np.zeros(Nv)


class VNode(object):
    def __init__(self):
        self.firtstedge = NULL
        self.data = NULL


class AdjVNode(object):
    def __init__(self, Adjv, Weight, next):
        self.Adjv = Adjv
        self.Weight = Weight
        self.next = next


class LGraph(object):
    def __init__(self, N):
        pass
