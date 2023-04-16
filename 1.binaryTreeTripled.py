#Write a function/method to make all leaves in a binary tree tripled.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tripleLeaves(root):
    if not root:
        return
    
    if not root.left and not root.right:
        root.val *= 3
    
    tripleLeaves(root.left)
    tripleLeaves(root.right)

    return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

modified_tree = tripleLeaves(root)
print(modified_tree.left.left.val)  
print(modified_tree.left.right.val)  
print(modified_tree.right.left.val)  
print(modified_tree.right.right.val)  
