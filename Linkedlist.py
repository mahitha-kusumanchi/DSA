class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtBeginning(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
    def insertAtEnd(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=node
    def printLinkedList(self):
        if self.head==None:
            print("Empty Linked List")
        temp=self.head
        llst=""
        while temp:
            llst+=str(temp.data)+"-->"
            temp=temp.next
        print(llst)
    def deleteAtBeginning(self):
        if self.head==None:
            print("No element to delete")
        else:
            self.head=(self.head).next
    def deleteAtEnd(self):
        if self.head==None:
            print("No element to delete")
        else:
            temp=self.head
            while (temp.next).next!= None:
                temp=temp.next
            temp.next=None
    def deleteAtIndex(self,index):
        if index>self.Size() and index<0:
            print("Invalid index")
        elif index==0:
            self.deleteAtBeginning()
        elif index==self.Size()-1:
            self.deleteAtEnd()
        else:
            itr=self.head
            num=0
            while num<index-1:
                num+=1
                itr=itr.next
            itr.next=itr.next.next
    def insertAtIndex(self,index,data):
        if index<0 or index>self.Size()-1:
            print("Invalid syntax")
        elif index==0:
            self.insertAtBeginning(data)
        elif index==self.Size():
            self.insertAtEnd(data)
        else:
            node = Node(data)
            num=0
            itr=self.head
            while num<index-1:
                itr=itr.next
                num+=1
            node.next=itr.next
            itr.next=node
    def Size(self):
        num=0
        temp=self.head
        while temp:
            num+=1
            temp=temp.next
        return num
if __name__=="__main__":
    linkedList=LinkedList()
    linkedList.insertAtBeginning(10)
    linkedList.insertAtBeginning(20)
    linkedList.insertAtBeginning(30)
    linkedList.printLinkedList()
    linkedList.insertAtEnd(0)
    linkedList.insertAtEnd(-10)
    linkedList.printLinkedList()
    print("-")
    linkedList.deleteAtBeginning()
    linkedList.printLinkedList()
    print("-")
    linkedList.deleteAtIndex(1)
    linkedList.printLinkedList()
    print("-")
    linkedList.insertAtIndex(1,100)
    linkedList.printLinkedList()
