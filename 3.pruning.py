# Implement a pruning function/method which takes in a binary tree t and a depth k, and should return a new tree that is a copy of only the first k levels of t. For example, if t is the tree shown as follows, then pruning(t, 3) should return the new tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def prune(t, k):
    if not t:
        return None
    
    if k == 0:
        return None
    
    node = TreeNode(t.val)
    node.left = prune(t.left, k - 1)
    node.right = prune(t.right, k - 1)
    
    return node

def print_tree(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result



t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)

pruned_tree = prune(t, 2)

print(print_tree(pruned_tree))  
