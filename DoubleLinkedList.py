class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=node
        node.prev=last
    def insertAtBeginning(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        self.head.prev=node
        node.next=self.head
        self.head=node
    def Size(self):
        num = 0
        temp = self.head
        while temp:
            num += 1
            temp = temp.next
        return num
    def insertAtindex(self,index,data):
        if index < 0 or index > self.Size() - 1:
            print("Invalid syntax")
        elif index == 0:
            self.insertAtBeginning(data)
        elif index == self.Size():
            self.insertAtEnd(data)
        else:
            node=Node(data)
            num=0
            itr=self.head
            while num<index-1:
                itr=itr.next
                num+=1
            node.next=itr.next
            node.prev=itr
            itr.next.prev=node
            itr.next=node
    def printLinkedList(self):
        if self.head == None:
            print("Empty Linked List")
            return
        temp = self.head
        llst = ""
        while temp:
            llst += str(temp.data) + "-->"
            temp = temp.next
        print(llst)
    def deleteAtIndex(self,index):
        if index > self.Size() and index < 0:
            print("Invalid index")
            return
        elif index == 0:
            self.deleteAtBeginning()
        elif index == self.Size() - 1:
            self.deleteAtEnd()
        else:
            itr = self.head
            for _ in range(index - 1):
                itr = itr.next
            to_delete = itr.next
            itr.next = to_delete.next
            if to_delete.next:
                to_delete.next.prev = itr
    def deleteAtBeginning(self):
        if self.head==None:
            print("No Element to delete")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head=self.head.next
                self.head.prev=None
    def deleteAtEnd(self):
        if self.head==None:
            print("No Element to delete")
        elif self.head.next is None:
            self.head = None
        else:
            itr=self.head
            while itr.next.next:
                itr=itr.next
            itr.prev.next=None
            itr.next=None
if __name__=="__main__":
    doublyLinkedList=DoublyLinkedList()
    doublyLinkedList.insertAtBeginning(0)
    doublyLinkedList.insertAtBeginning(10)
    doublyLinkedList.insertAtBeginning(20)
    doublyLinkedList.printLinkedList()
    doublyLinkedList.insertAtEnd(-10)
    doublyLinkedList.insertAtEnd(-20)
    doublyLinkedList.printLinkedList()
    print("-")
    doublyLinkedList.insertAtindex(2,100)
    doublyLinkedList.printLinkedList()
    doublyLinkedList.deleteAtIndex(3)
    doublyLinkedList.printLinkedList()
    doublyLinkedList.deleteAtBeginning()
    doublyLinkedList.printLinkedList()
    doublyLinkedList.deleteAtEnd()
    doublyLinkedList.printLinkedList()
