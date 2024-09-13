from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree:
    def buildTree(self,values):
        if values[0] is None:
            return None
        root=TreeNode(values[0])
        q=deque([root])
        i=1
        while i<len(values):
            temp=q.popleft()
            if i<len(values) and values[i] is not None:
                temp.left=TreeNode(values[i])
                q.append(temp.left)
            i+=1
            if i<len(values) and values[i] is not None:
                temp.right=TreeNode(values[i])
                q.append(temp.right)
            i+=1
        return root
    def preorder(self,root):
        if not root:
            return
        print(root.value,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
        return
    def postorder(self,root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=" ")
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value, end=" ")
        self.inorder(root.right)
    def depthFirst(self,root):
        if not root:
            return
        stack=deque([root])
        while stack:
            temp=stack.pop()
            print(temp.value,end=" ")
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
    def size(self,root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1+self.size(root.left)+self.size(root.right)
    def height(self,root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1+max(self.height(root.left),self.height(root.right))
    def countLeaves(self,root):
        if not root :
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countLeaves(root.left)+self.countLeaves(root.right)
    def level_order_helper(self, root):
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            temp = q.popleft()
            result.append(temp.value)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return result
    def print_level_order(self, root):
        values = self.level_order_helper(root)
        print(" ".join(map(str, values)))
    def clone(self, root):
        if not root:
            return None
        new_root = TreeNode(root.value)
        new_root.left = self.clone(root.left)
        new_root.right = self.clone(root.right)
        return new_root
    def printMirror(self, root):
        cloned_root = self.clone(root)
        self.mirror(cloned_root)
        values = self.level_order_helper(cloned_root)
        print(" ".join(map(str, values)))
    def mirror(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
    def isFullTree(self,root):
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left and root.right:
            return self.isFullTree(root.left) and self.isFullTree(root.right)
        return False

    def findAncestors(self, root, target):
        if root is None:
            return False
        if root.value == target:
            return True
        if self.findAncestors(root.left, target) or self.findAncestors(root.right, target):
            print(root.value, end=" ")
            return True
        return False
if __name__=="__main__":
    bt=BinaryTree()
    _values=input().split()
    values=[]
    for x in _values:
        if x != 'None':
            values.append(int(x))
        else:
            values.append(None)
    root=bt.buildTree(values)
    print("Level Order traversal :",end=" ")
    bt.print_level_order(root)
    print("preorder traversal :",end=" ")
    bt.preorder(root)
    print()
    print("postorder traversal :",end=" ")
    bt.postorder(root)
    print()
    print("inorder traversal :",end=" ")
    bt.inorder(root)
    print()
    print("depth first traversal :",end=" ")
    bt.depthFirst(root)
    print()
    print("size :",end=" ")
    print(bt.size(root))
    print("height ",end=" ")
    print(bt.height(root))
    print("number of leaves :",end=" ",)
    print(bt.countLeaves(root))
    print("is full tree :",end=" ")
    print(bt.isFullTree(root))
    print("Mirror Tree:", end=" ")
    print(bt.printMirror(root))
    print("Ancestors :",end=" ")
    print(bt.findAncestors(root,5))
