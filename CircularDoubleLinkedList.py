class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CircularDoubleLinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0
    def isEmpty(self):
        return self.front is None
    def enqueue(self,data):
        node=Node(data)
        if self.front is None:
            self.front=self.rear=node
            self.front.next=self.rear
            self.rear.prev=self.front
            self.rear.next=self.front
            self.front.prev=self.rear
        else:
            self.rear.next=node
            node.prev=self.rear
            self.rear=node
            node.next=self.front
            self.front.prev=self.rear
        self.count+=1
        print(f"enqueue : {data}")
    def size(self):
        print(f"size : {self.count}")
        return self.count
    def display(self):
        if self.isEmpty():
            print("Circular Double LinkedList is empty")
            return
        temp = self.front
        data = "<--> "
        while temp:
            data+=str(temp.data)+" <--> "
            temp=temp.next
            if temp is self.front:
                break
        print(data)
        return
    def displayReverse(self):
        if self.isEmpty():
            print("Circular Double LinkedList is empty")
            return
        temp = self.rear
        data = "<--> "
        while temp:
            data += str(temp.data) + " <--> "
            temp = temp.prev
            if temp is self.rear:
                break
        print(data)
        return
    def dequeue(self):
        if  self.isEmpty():
            print("Circular Double LinkedList is empty, dequeue can't be done ")
            return None
        node=self.front
        if self.front==self.rear:
            self.front = self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=self.rear
            self.rear.next=self.front
        print(f"dequeue : {node.data}")
        self.count-=1
        return node.data
if __name__=="__main__":
    cdl=CircularDoubleLinkedList()
    cdl.dequeue()
    cdl.enqueue(0)
    cdl.dequeue()
    cdl.enqueue(10)
    cdl.enqueue(20)
    cdl.display()
    cdl.displayReverse()
    cdl.size()
    cdl.dequeue()
    cdl.display()
