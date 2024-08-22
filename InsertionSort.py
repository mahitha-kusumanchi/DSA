def InsertionSort(Array):
    for i in range(1,len(Array)):
        j=i-1
        a=Array[i]
        while j>=0 and a<Array[j]:
            Array[j+1]=Array[j]
            j-=1
        Array[j+1]=a
    return Array
A=[3,7,2,9,1]
print(InsertionSort(A))

//or

class solution:
    def insert(self,Array,index,value):
        while (index>=0 and Array[index]>value):
            Array[index+1]=Array[index]
            index-=1
        Array[index+1]=value        
    def insertionSort(self,Array):
        for i in range(1,len(Array)):
            index=i-1
            value=Array[i]
            self.insert(Array,index,value)
        return Array
A=[3,7,2,9,1]
print(solution().insertionSort(A))


