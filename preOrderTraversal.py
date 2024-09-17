class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preOrderTraversal(node):
    li=[]
    def preOrder(node):
        li.append(node.data)
        if node.left:
            preOrder(node.left)
        if node.right:
            preOrder(node.right)
    if node:
        preOrder(node)
    return li


#or

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preOrder(node):
    print(node.data,end=" ")
    if node.left:
        preOrder(node.left)
    if node.right:
        preOrder(node.right)
if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(preOrder(root))
