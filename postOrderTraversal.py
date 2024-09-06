class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postOrderTraversal(node):
    li=[]
    def postOrder(node):
        if node.left:
            postOrder(node.left)
        if node.right:
            postOrder(node.right)
        li.append(node.data)
    if node:
        postOrder(node)
    return li
