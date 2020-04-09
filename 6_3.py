#
# 利用邻接矩阵表示图
#
# 输入格式
# Nv Ne
# V1 V2 Weight


import numpy as np
MaxVertexNum = 10


class Enode(object):
    def __init__(self, V1, V2, Weight):
        self.V1 = V1
        self.V2 = V2
        self.Weight = Weight


class MGraph(object):
    def __init__(self, N):
        self.G = np.zeros([N, N])

    def InsertEdge(self, Enode):
        self.G[Enode.V1][Enode.V2] = Enode.Weight
        self.G[Enode.V2][Enode.V1] = Enode.Weight




if __name__ == "__main__":
