class Node:
    def _init_(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def _init_(self):
        self.head=None
    def InsertAtBeginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        temp=self.head
        llst=''
        if (temp==None):
            return "Linked List is empty"
        while(temp):
            llst+=str(temp.data)+"-->"
            temp=temp.next
        return llst
    def DeleteAtBeginning(self):
        temp=self.head
        self.head=temp.next
    def top(self):
        if self.head==None:
            return "No top"
        return (self.head).data
    def size(self):
        if (self.head==None):
            return 0
        temp=self.head
        i=0
        while(temp):
            i+=1
            temp=temp.next
        return i
    def isEmpty(self):
            return self.size()==0

if _name=="main_":
    l1=LinkedList()
    print(l1.isEmpty())
    print(l1.print())
    l1.InsertAtBeginning(10)
    l1.InsertAtBeginning(20)
    l1.InsertAtBeginning(30)
    print(l1.print())
    l1.DeleteAtBeginning()
    print(l1.print())
    print(l1.top())
    print(l1.size())
    print(l1.isEmpty())
