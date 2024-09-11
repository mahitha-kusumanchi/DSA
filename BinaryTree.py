from collections import deque
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    q=deque([root])
    i=1
    while i<len(values):
        current=q.popleft()
        if i<len(values) and values[i] is not None:
            current.left=TreeNode(values[i])
            q.append(current.left)
        i+=1
        if i<len(values) and values[i] is not None:
            current.right=TreeNode(values[i])
            q.append(current.right)
        i+=1
    return root
def print_level_order(root):
    if not root:
        return
    q=deque([root])
    while q:
        node=q.popleft()
        print(node.value,end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
_values=input("Enter tree node values separated by space (use None for null nodes): ").split()
values=[]
for x in _values:
    if x!='None':
        values.append(int(x))
    else:
        values.append(None)
root=buildTree(values)
print("Level-order traversal of the tree:")
print_level_order(root)
