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

