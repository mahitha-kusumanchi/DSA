class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def level_order(root):
    if root is None:
        return
    queue=[root]
    while queue:
        current=queue.pop(0)
        print(current.data,end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print()
if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(7)
    level_order(root)
