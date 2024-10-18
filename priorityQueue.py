class PriorityQueue:
    def __init__(self):
        self.pq=[]
    def isEmpty(self):
        return not self.pq
    def getSize(self):
        return len(self.pq)
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0]
    def upHeap(self,childIndex):
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if self.pq[parentIndex]>self.pq[childIndex]:
                self.pq[parentIndex],self.pq[childIndex]=self.pq[childIndex],self.pq[parentIndex]
            else:
                break
            childIndex=parentIndex
    def insert(self,value):
        self.pq.append(value)
        childIndex=self.getSize()-1
        self.upHeap(childIndex)
    def buildMinHeap(self,values):
        for i in values:
            self.insert(i)
    def downHeap(self):
        parentIndex=0
        while True:
            leftChildIndex=2*parentIndex+1
            rightChildIndex=2*parentIndex+2
            minIndex=parentIndex
            if leftChildIndex<self.getSize() and self.pq[leftChildIndex]<self.pq[minIndex]:
                minIndex=leftChildIndex
            if rightChildIndex<self.getSize() and self.pq[rightChildIndex]<self.pq[minIndex]:
                minIndex=rightChildIndex
            if minIndex==parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex]=self.pq[minIndex],self.pq[parentIndex]
            parentIndex=minIndex
    def getHeap(self):
        print(self.pq)
    def removeMin(self):
        if self.isEmpty():
            return None
        ans=self.pq[0]
        if self.getSize()!=1:
            self.pq[0]=self.pq.pop()
            self.downHeap()
        else:
            self.pq.pop()
        return ans
    def heapSort(self) :
        tempHeap=self.pq.copy()
        sortedArray=[]
        while self.pq:
            sortedArray.append(self.removeMin())
        self.pq=tempHeap
        return sortedArray
    def getMaxHeapFromMinHeap(self):
        MaxHeap=self.pq.copy()
        size=len(MaxHeap)
        childIndex=size-1
        parentIndex=(childIndex-1)//2
        while parentIndex>=0:
            self.downHeapMax(MaxHeap,parentIndex,size)
            parentIndex-=1
        return MaxHeap
    def downHeapMax(self,heap,parentIndex,size):
        while True:
            leftChildIndex=2*parentIndex+1
            rightChildIndex=2*parentIndex+2
            maxIndex=parentIndex
            if leftChildIndex<size and heap[leftChildIndex] > heap[maxIndex]:
                maxIndex=leftChildIndex
            if rightChildIndex<size and heap[rightChildIndex] > heap[maxIndex]:
                maxIndex=rightChildIndex
            if maxIndex==parentIndex:
                break
            heap[parentIndex], heap[maxIndex] = heap[maxIndex], heap[parentIndex]
            parentIndex=maxIndex
if __name__=="__main__":
    pq=PriorityQueue()
    print("isEmpty :",end=" ")
    print(pq.isEmpty()) 
    print("get min :",end=" ") 
    print(pq.getMin())   
    print("get Size :",end=" ")
    print(pq.getSize())  
    values = [54,52,33,11,97,61]
    pq.buildMinHeap(values)
    print("Heap :",end=" ")
    pq.getHeap()      
    print("Heap sort :",end=" ")
    print(pq.heapSort())
    print("Remove min :",end=" ")   
    print(pq.removeMin())
    print("Heap :",end=" ")
    pq.getHeap()    
    print("get min :",end=" ") 
    print(pq.getMin()) 
    print("Heap sort :",end=" ")  
    print(pq.heapSort())
    print("Max heap :",end=" ")
    print(pq.getMaxHeapFromMinHeap())
    print("Heap :",end=" ")
    pq.getHeap() 
