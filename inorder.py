class treeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorderTraversal(node):
    li=[]
    def inorder(node):
        if node.left:
            inorder(node.left)
        li.append(node.data)
        if node.right:
            inorder(node.right)
    if node:
        inorder(node)
    return li
