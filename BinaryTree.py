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
    def preorder(self, root):
        if not root:
            return
        print(root.value, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=" ")
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value, end=" ")
        self.inorder(root.right)
    def depthFirst(self, root):
        if not root:
            return
        stack = deque([root])
        while stack:
            temp = stack.pop()
            print(temp.value, end=" ")
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
    def levelorder(self,root):
        values=self.level_order_helper(root)
        print(" ".join(map(str,values)))
    def levelOrderSpiral(self,root):
        if root is None:
            return []
        queue=[root]
        result=[]
        while queue:
            tempArraySize=len(queue)
            tempArray=[]
            for i in range(tempArraySize):
                node=queue.pop(0)
                tempArray.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tempArray)
        return result
    def zigZagTraversal(self,root):
        if root is None:
            return []
        queue=deque([root])
        result=[]
        leftToright=True
        while queue:
            tempArrSize=len(queue)
            tempArr=deque()
            for i in range(tempArrSize):
                if leftToright:
                    node = queue.popleft()
                    tempArr.append(node.value)
                else:
                    node = queue.popleft()
                    tempArr.appendleft(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            leftToright=not leftToright
            result.append(tempArr)
        return result
    def isLeaf(self,root):
        return root.left is None and root.right is None
    def boundaryTraversal(self,root):
        if root is None:
            return []
        a=self.leftMostTraversal(root)
        b=self.leaves(root)
        c=self.rightmost(root)
        return a+b+c
    def leftMostTraversal(self,root):
        if root is None:
            return []
        l=[]
        while root:
            if self.isLeaf(root):
                break
            l.append(root.value)
            if root.left:
                root=root.left
            else:
                root=root.right
        return l
    def leaves(self,root):
        leaves = []
        def collectLeaves(node):
            if node is None:
                return
            if self.isLeaf(node):
                leaves.append(node.value)
            collectLeaves(node.left)
            collectLeaves(node.right)
        collectLeaves(root)
        return leaves
    def rightmost(self,root):
        if root is None:
            return []
        l=[]
        while root:
            if self.isLeaf(root):
                break
            l.append(root.value)
            if root.right:
                root=root.right
            else:
                root=root.left
        if len(l) > 1:
            return l[1:][::-1]
        return []
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

    def countLeaves(self, root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countLeaves(root.left) + self.countLeaves(root.right)
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
    def level_order(self, root):
        values = self.level_order_helper(root)
        print(" ".join(map(str,values)))

    def clone(self,root):
        if not root:
            return None
        new_root=TreeNode(root.value)
        new_root.left=self.clone(root.left)
        new_root.right=self.clone(root.right)
        return new_root
    def mirror(self,root):
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)
    def printMirror(self, root):
        cloned_root = self.clone(root)
        self.mirror(cloned_root)
        values = self.level_order_helper(cloned_root)
        print(" ".join(map(str, values)))
    def findAncestors(self, root, target):
        if root is None:
            return False
        if root.value == target:
            return True
        if self.findAncestors(root.left, target) or self.findAncestors(root.right, target):
            print(root.value, end=" ")
            return True
        return False
    def findPath(self,root,target,path):
        if root is None:   # Base case: If root is None, there's no path
            return False
        path.append(root.value)   # Add current node to the path
        if root.value == target.value:  # Check if the current node is the target node
            return True
        if (self.findPath(root.left, target, path) or self.findPath(root.right, target, path)):  # Check if the target node is in the left or right subtree
            return True
        path.pop()  # If the target node is not in either subtree, remove the current node from path
        return False
    def getPath(self,root, target):
        path = []
        if self.findPath(root, target, path):
            return path
        else:
            return None
    def findLCA(self,root,node1,node2):
        if root is None:
            return None
        if root.value==node1.value or root.value==node2.value :
            return root
        leftLCA=self.findLCA(root.left,node1,node2)
        rightLCA=self.findLCA(root.right,node1,node2)
        if leftLCA and rightLCA:
            return root
        if leftLCA:
            return leftLCA
        else:
            return rightLCA
    def findParent(self,root,node):
        if root is None or node is None or root.value==node.value:
            return None
        if root.left and root.left.value==node.value :
            return root.value
        if  root.right and root.right.value==node.value:
            return root.value
        left_result = self.findParent(root.left, node)
        if left_result is not None:
            return left_result
        right_result = self.findParent(root.right, node)
        return right_result
    def findChildren(self,root,node):
        if root is None or node is None:
            return None
        if  root.value==node.value:
            li=[]
            if root.left:
                li.append(root.left.value)
            if root.right:
                li.append(root.right.value)
            return li
        left_result=self.findChildren(root.left,node)
        if left_result is not None:
            return left_result
        right_result = self.findChildren(root.right, node)
        return right_result
    def findSibling(self,root,node):
        if root is None or node is None or root.value == node.value:
            return None
        if root.left and root.left.value == node.value:
            if root.right:
                return root.right.value
        if root.right and root.right.value == node.value:
            if root.left:
                return root.left.value
        left_result = self.findSibling(root.left, node)
        if left_result is not None:
            return left_result
        right_result = self.findSibling(root.right, node)
        return right_result
    def findCousins(self,root,node):
        if root is None or node is None or root.value == node.value:
            return None
        queue=deque([root])
        marker=True
        while queue and marker:
            n=len(queue)
            for i in range(n):
                Node=queue.popleft()
                if (Node.left and Node.left.value==node.value) or (Node.right and Node.right.value==node.value) :
                    marker=False
                else:
                    if Node.left:
                        queue.append(Node.left)
                    if Node.right:
                        queue.append(Node.right)
        cousins=[]
        for i in queue:
            cousins.append(i.value)
        return cousins
    def findNode(self,root,node):
        if root is None or node is None:
            return None
        if root.value==node.value:
            return root
        left_result = self.findNode(root.left,node)
        if left_result is not None:
            return left_result
        right_result = self.findNode(root.right,node)
        if right_result is not None:
            return right_result
    def depthOfNode(self,root,node):
        Node=self.findNode(root,node)
        return self.height(Node)
    def descendents(self,root,node):
        Node=self.findNode(root,node)
        if Node is None:
            print("Node not found in the tree.")
            return
        queue=deque([Node])
        while queue:
            temp=queue.popleft()
            print(temp.value,end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    def findDiameter_(self,root,maxi):
        if root is None:
            return 0
        lh=self.findDiameter_(root.left,maxi)
        rh=self.findDiameter_(root.right,maxi)
        maxi[0]=max(maxi[0],lh+rh)
        return 1+max(lh,rh)
    def findDiameter(self,root):
        maxi=[0]
        self.findDiameter_(root, maxi)
        return maxi[0]
    def isFullTree(self,root):
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left and root.right:
            return self.isFullTree(root.left) and self.isFullTree(root.right)
        return False
    def CheckBalancedTree(self,root):
        if root is None:
            return 0
        left=self.CheckBalancedTree(root.left)
        right=self.CheckBalancedTree(root.right)
        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
    def isBalancedTree(self,root):
        return self.CheckBalancedTree(root)!=-1
    def isDegenerateTree(self,root):
        if root is None:
            return True
        while root:
            if root.left and root.right:
                return False
            if root.left:
                root=root.left
            else:
                root=root.right
        return True
    def isPerfect(self,root):
        def findDepth(node): # Calculate the depth of the leftmost leaf
            depth=0
            while node is not None:
                depth+=1
                node=node.left
            return depth
        def checkPerfect(node,depth,level=0):
            if node is None:
                return True
            if node.left is None and node.right is None: # Check if leaf node is at the correct depth
                return depth==level+1
            if node.left is None or node.right is None: # Check if internal node has both children
                return False
            return checkPerfect(node.left,depth,level+1) and checkPerfect(node.right,depth,level+1)
        depth=findDepth(root)
        return checkPerfect(root,depth)
    def isComplete(self,root):
        if not root:
            return True
        queue=deque([root])
        end=False  # This flag indicates if we have seen a non-complete node
        while queue:
            current=queue.popleft()
            if current.left:
                if end:  # If we have seen a non-complete node, and now we see a child, it's not complete
                    return False
                queue.append(current.left)
            if current.right:
                if end: # If there was no left child before, it means the tree is not complete
                    return False
                queue.append(current.right)
            else:
                end=True  # We have seen a non-complete node (no right child)
        return True
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
    bt.level_order(root)
    print("Level Order spiral traversal :",end=" ")
    print(bt.levelOrderSpiral(root))
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
    print("zig zag traversal ",end=" ")
    print(bt.zigZagTraversal(root))
    print("leaves: ", end=" ")
    print(bt.leaves(root))
    print("left most :", end=" ")
    print(bt.leftMostTraversal(root))
    print("right most", end=" ")
    print(bt.rightmost(root))
    print("boundary traversal ", end=" ")
    print(bt.boundaryTraversal(root))
    print("size :",end=" ")
    print(bt.size(root))
    print("height ",end=" ")
    print(bt.height(root))
    print("number of leaves :",end=" ",)
    print(bt.countLeaves(root))
    print("Mirror Tree:", end=" ")
    print(bt.printMirror(root))
    print("Ancestors :", end=" ")
    print(bt.findAncestors(root, 5))
    print("path :",end=" ")
    print(bt.getPath(root,TreeNode(2)))
    print("parent ", end=" ")
    print(bt.findParent(root, TreeNode(5)))
    print("children ", end=" ")
    print(bt.findChildren(root, TreeNode(2)))
    print("siblings :", end=" ")
    print(bt.findSibling(root, TreeNode(2)))
    print("descendents :", end=" ")
    bt.descendents(root, TreeNode(3))
    print("\ndepth :", end=" ")
    print(bt.depthOfNode(root, TreeNode(4)))
    print("cousins :", end=" ")
    print(bt.findCousins(root, TreeNode(5)))
    print("LCA :", end=" ")
    print(bt.findLCA(root, TreeNode(2), TreeNode(3)).value)
    print("Diameter : ",end=" ")
    print(bt.findDiameter(root))
    print("is full tree :", end=" ")
    print(bt.isFullTree(root))
    print("is Balanced Tree: ",end=" ")
    print(bt.isBalancedTree(root))
    print("is degenerate tree",end=" ")
    print(bt.isDegenerateTree(root))
    print("is perfect :",end=" ")
    print(bt.isPerfect(root))
    print("is complete :",end=" ")
    print(bt.isComplete(root))
