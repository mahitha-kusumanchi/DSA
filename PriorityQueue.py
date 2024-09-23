#min heap
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
    def upheap(self,index):
        while index>0:
            parentIndex=(index-1)//2
            if self.pq[parentIndex]>self.pq[index]:
                self.pq[parentIndex],self.pq[index]=self.pq[index],self.pq[parentIndex]
                index=parentIndex
            else:
                break
    def insert(self,value):
        self.pq.append(value)
        self.upheap(self.getSize()-1)
    def buildHeap(self,values):
        for value in values:
            self.insert(value)
    def getHeap(self):
        print(self.pq)
    def downHeap(self):
        parentIndex=0
        size=self.getSize()
        while True:
            minIndex=parentIndex
            leftChildIndex=2*parentIndex+1
            rightChildIndex=2*parentIndex+2
            if leftChildIndex<size and self.pq[leftChildIndex]<self.pq[parentIndex]:
                minIndex=leftChildIndex
            if rightChildIndex<size and self.pq[rightChildIndex]<self.pq[parentIndex]:
                minIndex=rightChildIndex
            if minIndex==parentIndex:
                break
            self.pq[minIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[minIndex]
    def removeMin(self):
        if self.isEmpty():
            return None
        ans=self.pq[0]
        if self.getSize()==1:
            self.pq.pop()
        else:
            self.pq[0]=self.pq.pop()
            self.downHeap()
        return ans
    def heapSort(self):
        sortedArray=[]
        tempArray=self.pq.copy()
        while self.pq:
            sortedArray.append(self.removeMin())
        self.pq=tempArray
        return sortedArray
    def getSortedHeap(self):
        print(self.heapSort())
    def kthSmallest(self,k):
        if k<0 or k>self.getSize():
            return
        array=self.heapSort()
        print(array[k-1])
    def MinHeaptoMaxHeap(self):
        tempArray=self.pq.copy()
        MaxHeap=[]
        for i in self.pq:
            self.insertMaxHeap(MaxHeap,i)
        self.pq=tempArray
        print(MaxHeap)
    def insertMaxHeap(self,Heap,value):
        Heap.append(value)
        size=len(Heap)
        childIndex=size-1
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if Heap[parentIndex]<Heap[childIndex]:
                Heap[parentIndex],Heap[childIndex]=Heap[childIndex],Heap[parentIndex]
                childIndex=parentIndex
            else:
                break        
if __name__=="__main__":
    pq=PriorityQueue()
    values=[98,45,13,5,86,53,64,90]
    pq.buildHeap(values)
    pq.getHeap()
    pq.removeMin()
    pq.getHeap()
    pq.getSortedHeap()
    pq.kthSmallest(2)
    pq.MinHeaptoMaxHeap()
