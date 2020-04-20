#
# 哈利波特的考试 （计算任意两点间的最短路径）
#
# 输入样例：
# 6 11    (6个点 11条边)
# 3 4 70
# 1 2 1
# 5 4 50
# 2 6 50
# 5 6 60
# 1 3 70
# 4 6 60
# 3 6 80
# 5 1 100
# 2 4 60
# 5 2 80
#
#
# 输出样例：
# 4 70 （从4出发，最长的点也只有70，是各个点最长的里面最短的）
#
# PS.  使用Floyd算法

import numpy as np
MaxVertexNum = 100
INFINITY = 65535


class Enode(object):
    def __init__(self, V1, V2, Weight):
        self.V1 = V1
        self.V2 = V2
        self.Weight = Weight


class MGraph(object):
    def __init__(self, Nv,Ne):
        self.G = np.full((Nv, Nv), INFINITY)
        self.Nv = Nv # 顶点数
        self.Ne = Ne # 边数

    def InsertEdge(self, Enode):
        i = Enode.V1 - 1  # 题目编号从1开始，数组编号从0开始
        j = Enode.V2 - 1
        self.G[i][j] = Enode.Weight
        self.G[j][i] = Enode.Weight

    def Floyd(self):
        self.D = self.G[:][:]

        for i in np.arange(0, self.Nv, 1):
            for j in np.arange(0, self.Nv, 1):
                for k in np.arange(0, self.Nv, 1):
                    if D[i][k]+D[k][j] < D[i][j]:
                        D[i][j] = D[i][k]+D[k][j]

    def FindMin(self):
        MinDist = INFINITY
        for i in np.arange(0, self.Nv, 1):
            MaxDist = self.FindMaxDist(i)
            if MaxDist == INFINITY:
                print("0")
                return
            if MinDist > MaxDist:
                MinDist = MaxDist
                Animal = i+1

    
    def FindMaxDist(self, i): # i 表示行数
        MaxDist = 0
        for j in np.arange(0, self.Nv, 1):
            if D[i][j] > MaxDist:
                MaxDist = D[i][j]
        return MaxDist

if __name__ == "__main__":
