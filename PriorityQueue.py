#minHeap
class PriorityQueue:
    def __init__(self) -> None:
        self.pq=[]
    def isEmpty(self):
        return len(self.pq)==0
    def getMin(self):
        if not self.pq:
            return None
        return self.pq[0]
    def getSize(self):
        return len(self.pq)
    def buildHeap(self,values):
        for i in values:
            self.insert(i)
    def getHeap(self):
        print(self.pq)
    def insert(self,element):
        self.pq.append(element)
        childIndex=self.getSize()-1
        while(childIndex>0):
            parentIndex=(childIndex-1)//2
            if self.pq[childIndex]<self.pq[parentIndex]:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
            else:
                break
            childIndex=parentIndex
    def removeMin(self):
        size=self.getSize()
        if size==0:
            return None
        ans=self.pq[0]
        self.pq[0]=self.pq.pop()
        parentIndex=0
        size-=1
        while True:
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2
            minIndex = parentIndex
            if leftChildIndex < size and self.pq[leftChildIndex] < self.pq[minIndex]:
                minIndex = leftChildIndex
            if rightChildIndex < size and self.pq[rightChildIndex] < self.pq[minIndex]:
                minIndex = rightChildIndex
            if minIndex == parentIndex:
                break
            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex = minIndex
        return ans     
if __name__=="__main__":
    pq=PriorityQueue()
    print(pq.isEmpty())
    print(pq.getMin())
    print(pq.getSize())
    values=[4,52,57,10,24,54]
    pq.buildHeap(values)
    pq.getHeap()
    pq.removeMin()            
    pq.getHeap()
    print(pq.getMin())
    
#maxHeap

class PriorityQueue:
    def __init__(self) -> None:
        self.pq=[]
    def getSize(self):
        return len(self.pq)
    def isEmpty(self):
        return not self.pq
    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0]
    def buildMaxHeap(self,values):
        for i in values:
            self.insert(i)
    def insert(self,value):
        self.pq.append(value)
        childIndex=self.getSize()-1
        while childIndex>0:
            parentIndex=(childIndex-1)//2
            if self.pq[parentIndex]<self.pq[childIndex]:
                self.pq[parentIndex],self.pq[childIndex]=self.pq[childIndex],self.pq[parentIndex]
            else:
                break
            childIndex=parentIndex
    def removeMax(self):
        if self.isEmpty():
            return None
        ans=self.pq[0]
        self.pq[0]=self.pq.pop()
        size=self.getSize()
        parentIndex=0
        while True:
            leftChildIndex=2*parentIndex+1
            rightChildIndex=2*parentIndex+2
            maxIndex=parentIndex
            if leftChildIndex<size and self.pq[maxIndex]<self.pq[leftChildIndex]:
                maxIndex=leftChildIndex
            if rightChildIndex<size and self.pq[maxIndex]<self.pq[rightChildIndex]:
                maxIndex=rightChildIndex
            if maxIndex==parentIndex:
                break
            self.pq[parentIndex],self.pq[maxIndex]=self.pq[maxIndex],self.pq[parentIndex]
            parentIndex=maxIndex
        return ans
    def getHeap(self):
        print(self.pq)
if __name__=="__main__":
    pq=PriorityQueue()
    print(pq.isEmpty())
    print(pq.getMax())
    print(pq.getSize())
    values=[4,52]
    pq.buildMaxHeap(values)
    pq.getHeap()
    print(pq.removeMax())
    pq.getHeap()
    print(pq.getMax())   
            
