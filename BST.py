class TreeNode:
    def __init__(self,value) -> None:
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self) -> None:
        self.root=None
    def insert(self,value):
        if self.root is None:
            self.root=TreeNode(value)
        else:
            temp=self.root
            while temp:
                if temp.value>value:
                    if temp.left:
                        temp=temp.left
                    else:
                        temp.left=TreeNode(value)
                        break
                elif temp.value<value:
                    if temp.right:
                        temp=temp.right
                    else:
                        temp.right=TreeNode(value)
                        break
    def buildBST(self,values):
        for i in values:
            self.insert(i)
    def _inorder(self,root):
        if root is None:
            return
        self._inorder(root.left)
        print(root.value,end=" ")
        self._inorder(root.right)
    def inorder(self):
        self._inorder(self.root)
    def _findMin(self,root):
        if root is None:
            return None
        while root:
            if root.left is None:
                return root.value
            root=root.left
    def findMin(self):
        print(self._findMin(self.root))
    def _findMax(self,root):
        if root is None:
            return None
        while root:
            if root.right is None:
                return root.value
            root=root.right
    def findMax(self):
        print(self._findMax(self.root))
    def _search(self,root,value):
        while root :
            if root.value==value:
                return root.value
            elif root.value>value:
                root=root.left
            else:
                root=root.right
        return -1
    def search(self,value):
        print(self._search(self.root,value))
    def _ceil(self,root,value):
        #value of the smallest node in the BST that is greater than or equal to the given key.
        ceil=-1
        while root:
            if root.value==value:
                ceil=root.value
                break
            elif root.value>value:
                ceil=root.value
                root=root.left
            else:
                root=root.right
        return ceil
    def ceil(self,value):
        print(self._ceil(self.root,value))
    def _floor(self,root,value):
        #value of the largest node in the BST that is smaller than or equal to the given key.
        floor=-1
        while root:
            if root.value==value:
                floor=root.value
                break
            elif root.value>value:
                root=root.left
            else:
                floor=root.value
                root=root.right
        return floor
    def floor(self,value):
        print(self._floor(self.root,value))
    def findLastRight(self,root):
        if root.right is None:
            return root
        return self.findLastRight(root.right)
    def helper(self,root):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        rightChild=root.right
        lastRight=self.findLastRight(root.left)
        lastRight.right=rightChild
        return root.left
    def _deleteNode(self, root, key):
        if root is None:
            return None
        if root.value==key:
            return self.helper(root)
        temp=root
        while root:
            if root.value>key:
                if root.left and root.left.value==key:
                    root.left=self.helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right and root.right.value==key:
                    root.right=self.helper(root.right)
                    break
                else:
                    root=root.right
        return temp
    def deleteNode(self,key):
        self._deleteNode(self.root,key)
if __name__=="__main__":
    bst=BST()
    values=[2,45,72,27,19,56]
    bst.buildBST(values)
    print("inorder :",end=" ")
    bst.inorder()
    print("\nmin value :",end=" ")
    bst.findMin()
    print("max value :",end=" ")
    bst.findMax()
    print("search :",end=" ")
    bst.search(4)
    print("ceil :",end=" ")
    bst.ceil(25) 
    print("Floor ",end=" ")
    bst.floor(25)
    print("Delete Node : ",end=" ")
    bst.deleteNode(19)
    bst.search(19)
  
