def MergeSort(Array,low,high):
    if low<high:
        mid=(low+high)//2
        MergeSort(Array,low,mid)
        MergeSort(Array,mid+1,high)
        Merge(Array,low,mid,high)
    return Array
def Merge(Array,low,mid,high):
    i=j=0
    k=low
    left=Array[low:mid+1]
    right=Array[mid+1:high+1]
    while (i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            Array[k]=left[i]
            i+=1
        else:
            Array[k]=right[j]
            j+=1
        k+=1
    while (i<len(left)):
        Array[k]=left[i]
        i+=1
        k+=1
    while (j<len(right)):
        Array[k]=right[j]
        j+=1
        k+=1
A=[3,8,1,9,2,7,4]
print(MergeSort(A,0,len(A)-1))

#Using classes and Objects

class Solution:
    def MergeSort(self,Array,low,high):
        if low<high:
            mid=(low+high)//2
            self.MergeSort(Array,low,mid)
            self.MergeSort(Array,mid+1,high)
            self.Merge(Array,low,mid,high)
        return Array
    def Merge(self,Array,low,mid,high):
        i=j=0
        k=low
        left=Array[low:mid+1]
        right=Array[mid+1:high+1]
        while (i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                Array[k]=left[i]
                i+=1
            else:
                Array[k]=right[j]
                j+=1
            k+=1
        while (i<len(left)):
            Array[k]=left[i]
            i+=1
            k+=1
        while (j<len(right)):
            Array[k]=right[j]
            j+=1
            k+=1
A=[3,8,1,9,2,7,4]
print(Solution().MergeSort(A,0,len(A)-1))

#another approach

def mergeSort(Arr):
    if len(Arr)<=1:
        return Arr
    mid=(len(Arr))//2
    left=mergeSort(Arr[:mid])
    right=mergeSort(Arr[mid:])
    return merge(left,right)
def merge(leftArray,rightArray):
    i=j=0
    Array=[]
    while i<len(leftArray) and j<len(rightArray):
        if leftArray[i]<rightArray[j]:
           Array.append(leftArray[i])
           i+=1
        else:
            Array.append(rightArray[j])
            j+=1
    Array.extend(leftArray[i:])
    Array.extend(rightArray[j:])
    return Array
arr=[4,1,9,0]
print(mergeSort(arr))


