class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.count=0
        self.front=None
        self.rear=None
    def isEmpty(self):
        return self.count==0
    def isFull(self):
        return self.count==self.capacity
    def Enqueue(self,data):
        node=Node(data)
        if self.isFull():
            print(f"Queue is full,{data} can't be added")
            return
        if self.front is None:
            self.front=self.rear=node
            self.rear.next=self.front
        else:
            self.rear.next=node
            self.rear=node
            self.rear.next=self.front
        self.count+=1
        print(f"Enqueue data : {data}")
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty ,Dequeue is not possible")
            return
        data=self.front.data
        if self.count==1:
            self.front=self.rear=None
        else:
            self.front=self.front.next
            self.rear.next=self.front
        print(f"dequeue data : {data}")
        self.count-=1
        return data
    def Front(self):
        if self.count==0:
            print("No front element")
            return None
        else:
            data=self.front.data
            print(f"Front Element :{data} ")
            return data
    def Rear(self):
        if self.count==0:
            print("No Rear element")
            return None
        else:
            data=self.rear.data
            print(f"Rear Element :{data} ")
            return data
    def size(self):
        print(f"size={self.count}")
        return self.count
    def clear(self):
        self.front=None
        self.rear=None
        self.count=0
        print("Circular Queue cleared")
    def display(self):
        if self.count==0:
            print("Circular Queue is Empty")
            return None
        data=""
        temp=self.front
        while temp:
            data+=str(temp.data)+"-->"
            temp=temp.next
            if temp is self.front:
                break
        print(data)
