# 寻找打电话最多的人
#
#
# 输入样例：
# 4
# 13005711862 13588625832
# 13505711862 13088625832
# 13588625832 18087925832
# 15005713862 13588625832
#
#
# 输出样例：
# 13588625832
#
# ps 使用分析链接法的散列表

import math as m
import numpy as np
import string 

NULL = -1
KEYLENGTH = 11
MAXTABLESIZE = 1000000

class ListNode(object):
    def __init__(self, value, next, count):
        self.value = value
        self.next = next
        self.count = count
        


class HashTbl(object):
    def __init__(self, size):
        self.size = self.NextPrime(size)  # 表的最大长度
        self.Head = [NULL] * self.size   # 指向链表头结点的数组
        for i in np.arange(0, self.size, 1):
            self.Head[i] = ListNode('\0', NULL, 0)
    
    def Insert(self,key):
        p  = self.Find(key)

        if P == NULL:
            pos = self.Hash(string.atio(key[-5:]),self.size)
            cell = ListNode(key, self.Head[pos].next, 1)
            print("insert successfully!")
        else:
            p.count += 1
            print("the node is existed.")


    def Hash(self, key, P):
        return key % P
    
    def NextPrime(self, N):
        # 返回大于N且不超过MAXTABLESIZE的最小素数
        if N % 2 == 1 :
            p = N+2
        else:
            p = N+1
        
        i = m.floor(m.sqrt(p))
        while( p <= MAXTABLESIZE):
            while(i > 2):
                if p % i == 0:
                    break
                i -= 1
            if i == 2:
                break
            else:
                p += 2
                
        return p

    def Find(self, key):
        pos = self.Hash(string.atio(key[-5:]),self.size)
        P = self.Head[pos].next

        while((p != NULL) && (p.value != key)):
            p = p.next
        return p


    def ScanAndOutput(self):
        pass

    def DestoryTable(self):
        pass



if __name__ == "__main__"：
    H = HashTbl(4*2)
