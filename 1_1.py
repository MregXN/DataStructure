# 
#   设计函数分别求两个一元多项式的乘积与和
#
#   输入样例：
#   4 3 4 -5 2 6 1 -2 0 （3x^4-5x^2-6x-2）
#   3 5 20 -7 4 3 1 （5x^20-7x^4+3x）
#   
#   输出样例：
#   15 24 -25 22 30 21 -10 20 -21 8 35 6 -33 5 14 4 -15 3 18 2 -6 1 
#   5 20 -4 4 -5 2 9 1 -2 0
# 
# 
#   ps:多项式表示可用数组或链表，比较简单的方法是动态数组,这里用户链表


import numpy as py

class Node(object):
    def __init__(self,coef=0,expon=0,pnext=0):
        self.coef = coef
        self.expon = expon
        self.next = pnext  


# self.head 节点中不放数据，作为链表头
class LinkList(object):
    def __init__(self):
        self.head = Node();

    def __getitem__(self,key):
        if self.is_empty():
            print(" linklist is empty.")
            return
        elif key < 0 or key > self.getlength():
            print("the given key is error")
            return          
        else:
            return self.getitem(key)

    def __setitme__(self,key,value):
        if self.is_empty():
            print(" linklist is empty.")
            return
        elif key < 0 or key > self.getlength():
            print("the given key is error")
            return            
        else:
            self.delete(key)
            return self.insert(key)
    
    def initlist(self,data):

        self.head.coef = data[0]
        p = self.head

        if len(data) > 1 :
            toggle_flag = True;
            for i in data[1:]:
                if  toggle_flag:
                    node = Node(coef=i,expon=0)
                else:
                    node.expon = i
                    p.next = node
                    p = p.next           
                toggle_flag = not toggle_flag

    def getlength(self):
        p = self.head
        length = 0
        while p.next != 0:
            length += 1
            p = p.next

        return length

    def is_empty(self):
        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self,coef,expon):
        node = Node(coef,expon)
        if self.head.next == 0:
            self.head.next  = node 
        else:
            p = self.head
            while p.next != 0 :
                p = p.next
            
            p.next = node 

        
    def getitem(self,index):
        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.coef,p.expon
        else:
            print('target is not exist!') 


    def insert(self,index,coef,expon):
        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return   

        if index == 0 :
            q = Node(coef,expon)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next !=0 and j < index :
            post = p
            p = p.next
            j+=1

        if index == j :
            q= Node(coef,expon)
            post.next = q
            q.next = p

    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = self.head 
            self.head = q.next

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next       

    def printall(self):
        length = self.getlength()
        i=0
        while length:
            i+=1
            print(self.getitem(i))
            length-=1



def add(l1,l2):

    p1 = l1
    p2 = l2
    sum = LinkList()

    while p1 and p2 :
        if p1.expon == p2.expon:
            if p1.coef + p2.coef != 0:
                sum.append(p1.coef + p2.coef , p1.expon )
                p1 = p1.next
                p2 = p2.next
        elif p1.expon > p2.expon:
            sum.append(p1.coef, p1.expon )
            p1 = p1.next
        else:
            sum.append(p2.coef, p2.expon )
            p2 = p2.next
        
    while(p1):
        sum.append(p1.coef, p1.expon )
        p1 = p1.next

    while(p2):
        sum.append(p2.coef, p2.expon )
        p2 = p2.next

    return sum


def multiple(l1,l2):
    p1 = l1
    p2 = l2
    result = LinkList()
    temp = LinkList()

    while p1 :
        while p2:
            temp.append(p1.coef*p2.coef,p1.expon+p2.expon)
            p2 = p2.next
        
        result = add(result.head.next,temp.head.next)

        p2 = l2
        p1 = p1.next
        temp = LinkList()

    return result

if __name__ == '__main__' :
    l1 = LinkList()
    l2 = LinkList()
    l1.initlist([ 4,3,4,-5,2,6,1,-2,0])
    l2.initlist([ 3,5,20,-7,4,3,1])

    # #multiple
    print("the result is : ")
    result = multiple(l1.head.next,l2.head.next) # 跳过头结点，从第一个数据开始
    result.printall()

    #add
    result = add(l1.head.next,l2.head.next) # 跳过头结点，从第一个数据开始
    print("the result is : ")
    result.printall()

