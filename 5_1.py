#
# File Transfer
# 给定若干计算机，经过连线，判断两台计算机是否在同一集合中（能否传输文件）
#
# 输入样例1:
# 5
# C 3 2
# I 3 2
# C 1 5
# I 4 5
# I 2 4
# C 3 5
# S
#
# 输出1：
# no
# no
# yes
# there are 2 components
#
# 输入样例2:
# 5
# C 3 2
# I 3 2
# C 1 5
# I 4 5
# I 2 4
# C 3 5
# I 1 3
# C 1 5
# S
#
# 输出2：
# no
# no
# yes
# yes
# the network is connected

NULL = -1


class Union(object):
    def __init__(self, num):
        self.union = [NULL] * (num + 1)
        self.union[0] = 999  # 下标为0的位置未使用

    def Find(self, node):
        # 路径压缩
        if self.union[node] < 0:
            return node
        else:
            self.union[node] = self.Find(self.union[node])
            return self.union[node]

    def InputConnection(self, node1, node2):
        # 按秩归并
        if self.union[self.Find(node2)] < self.union[self.Find(node1)]:
            self.union[self.Find(node1)] = self.Find(node2)
        else:
            self.union[self.Find(node1)] += self.union[self.Find(node2)]
            self.union[self.Find(node2)] = self.Find(node1)

    def CheckConnection(self, node1, node2):
        if self.Find(node1) == self.Find(node2):
            return "yes"
        else:
            return "no"

    def CheckNetwork(self):
        count = 0
        for i in self.union:
            if i < 0:
                count += 1

        if count == 1:
            return "the network is connected"
        else:
            return "there are %d components" % (count)

    def Cmd(self, input):
        if input[0] == 'C':
            print(self.CheckConnection(input[1], input[2]))
        elif input[0] == 'I':
            self.InputConnection(input[1], input[2])
        elif input[0] == 'S':
            print(self.CheckNetwork())


if __name__ == "__main__":
    U = Union(5)

    print("样例1：")
    U.Cmd(['C', 3, 2])
    U.Cmd(['I', 3, 2])

    U.Cmd(['C', 1, 5])
    U.Cmd(['I', 4, 5])

    U.Cmd(['I', 2, 4])
    U.Cmd(['C', 3, 5])

    U.Cmd(['S'])

    print("样例2：")
    U = Union(5)

    U.Cmd(['C', 3, 2])
    U.Cmd(['I', 3, 2])

    U.Cmd(['C', 1, 5])
    U.Cmd(['I', 4, 5])

    U.Cmd(['I', 2, 4])
    U.Cmd(['C', 3, 5])

    U.Cmd(['I', 1, 3])
    U.Cmd(['C', 1, 5])

    U.Cmd(['S'])   