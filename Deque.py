class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def isEmpty(self):
        return self.count==0
    def size(self):
        return self.count
    def insertFirst(self,data):
        node=Node(data)
        if self.front is None:
            self.front=self.rear=node
        else:
            node.next=self.front
            self.front=node
        self.count+=1
        print(f"insert first : {data}")
    def insertLast(self,data):
        node=Node(data)
        if self.rear is None:
            self.front=self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self.count+=1
        print(f"insert last : {data}")
    def removeFirst(self):
        if self.front is None:
            print("remove first is not possible")
            return
        data=self.front.data
        if self.count==1:
            self.front=self.rear=None
        else:
            self.front=self.front.next
        print(f"remove first : {data}")
        self.count-=1
        return data
    def removeLast(self):
        if self.rear is None:
            print("remove last is not possible")
            return
        data=self.rear.data
        if self.count==1:
            self.front=self.rear=None
        else:
            temp=self.front
            while temp.next != self.rear:
                temp=temp.next
            self.rear=temp
            self.rear.next=None
        print(f"remove last : {data}")
        self.count-=1
        return data
    def first(self):
        if self.count==0:
            print("Deque is Empty")
            return
        return self.front.data
    def last(self):
        if self.count==0:
            print("Deque is Empty")
            return
        return self.rear.data
