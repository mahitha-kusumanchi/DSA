// go through visualgo for understanding this code
class Solution: 
    def select(self, arr, i):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        return minIndex
    def selectionSort(self, arr):
        for i in range(len(arr)):
            minIndex=self.select( arr, i)
            arr[minIndex],arr[i]=arr[i],arr[minIndex]
        return arr
solution=Solution()
A=[3,7,2,9,0]
print(solution.selectionSort(A))

//or 

def Selection_Sort(Array):
    for i in range(len(Array)):
        small=i
        for j in range(i+1,len(Array)):
            if Array[j]<Array[small]:
                small=j
        Array[small],Array[i]=Array[i],Array[small]
    return Array
A=[3,7,2,9,0]
print(Selection_Sort(A))
