# 输入样例:
# 4 5 0 3   4个点 5条边 0位起点 3为终点
# 0 1 1 20
# 1 3 2 30
# 0 3 4 10
# 0 2 2 20
# 2 3 1 20
#
#
#

import numpy as np
MaxVertexNum = 100
INFINITY = 65535


class Enode(object):
    def __init__(self, V1, V2, Dist, Cost):
        self.V1 = V1
        self.V2 = V2
        self.Dist = Dist
        self.Cost = Cost


class MGraph(object):
    def __init__(self, Nv, Ne, Start, End):
        self.G = np.full((Nv, Nv), INFINITY)
        self.dist = [INFINITY] * Nv
        self.path = [-1] * Nv
        self.collect = [0] * Nv
        self.cost = [0] * Nv
        self.Nv = Nv  # 顶点数
        self.Ne = Ne  # 边数
        self.Start = Start  # 边数
        self.End = End  # 边数

        self.dist[Start] = 0
        self.cost[Start] = 0

    def InsertEdge(self, Enode):
        i = Enode.V1  # 题目编号从1开始，数组编号从0开始
        j = Enode.V2
        self.G[i][j] = Enode.Dist
        self.G[j][i] = Enode.Cost

    def Dijkstra(self):
        while 1:
            v = self.FindMinInDist()
            if v == -1:
                break
            self.collect[v] = 1

            for i in np.arange(0, self.Nv, 1):
                if self.collect[i] == 0:
                    if v < i:
                        dis = self.G[v][i]
                        cost = self.G[i][v]
                    else:
                        dis = self.G[i][v]
                        cost = self.G[v][i]

                    if self.dist[v] + dis < self.dist[i]:
                        self.dist[i] = self.dist[v] + dis
                        self.path[i] = v
                        self.cost[i] = self.cost[v] + cost
                    elif (self.dist[v] + dis == self.dist[i]) and (
                            self.cost[v] + cost < self.cost[i]):
                        self.cost[i] = self.cost[v] + cost
                        self.path[i] = v

    def FindMinInDist(self):
        pos = -1
        min = INFINITY
        for i in np.arange(0, self.Nv, 1):
            if self.collect[i] == 0:
                if self.dist[i] < min:
                    min = self.dist[i]
                    pos = i

        return pos

    def Output(self):
        self.Dijkstra()

        print("distance: %d"%G.dist[self.End])
        print("cost: %d"%G.cost[self.End])

if __name__ == "__main__":
    G = MGraph(4, 5, 0, 3)
    input = [0, 1, 1, 20, 1, 3, 2, 30, 0, 3, 4, 10, 0, 2, 2, 20, 2, 3, 1, 20]

    for i in np.arange(0, len(input), 1):
        if i % 4 == 0:
            a = input[i]
        elif i % 4 == 1:
            b = input[i]
        elif i % 4 == 2:
            c = input[i]
        else:
            d = input[i]
            G.InsertEdge(Enode(a, b, c, d))

    G.Output()
