class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def Enqueue(self,data):
        node=Node(data)
        if self.front is None:
            self.front=self.rear=node
        else:
            self.rear.next=node
            self.rear=node
    def PrintData(self):
        temp=self.front
        if temp is None:
            print("empty queue")
            return
        QueueRecord=""
        while temp:
            QueueRecord+=str(temp.data)+"-->"
            temp=temp.next
        print(QueueRecord)
    def Size(self):
        temp=self.front
        size=0
        if temp is None:
            return 0
        while temp:
            size+=1
            temp=temp.next
        return size
    def Dequeue(self):
        Size=self.Size()
        if Size == 0:
            print("deque not possible")
            return
        temp = self.front
        if Size==1:
            self.rear=self.front=None
            return temp.data
        self.front=self.front.next
        return temp.data
    def Front(self):
        if self.front:
            return self.front.data
        return None
    def Rear(self):
        if self.rear is None:
            return None
        return self.rear.data
    def clear(self):
        self.front=self.rear=None
    def isEmpty(self):
        return self.front is None
