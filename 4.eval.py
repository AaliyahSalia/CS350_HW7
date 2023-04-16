# The arithmetic expression can be converted to a binary tree structure, where all leaves are numbers and all inner-node labels are operators (just considering 7 operations: +, -, *, /, //, %, **), such as the following binary tree for the expression: 3 + ((5+9)*2). Define a function/method eval(t) to calculate the expression value denoted by t

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluate_expression(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.val)
    left_val = evaluate_expression(root.left)
    right_val = evaluate_expression(root.right)
    if root.val == "+":
        return left_val + right_val
    elif root.val == "-":
        return left_val - right_val
    elif root.val == "*":
        return left_val * right_val
    elif root.val == "/":
        return left_val / right_val
    elif root.val == "//":
        return left_val // right_val
    elif root.val == "%":
        return left_val % right_val
    elif root.val == "**":
        return left_val ** right_val
    else:
        raise ValueError("Invalid operator: " + root.val)


root = TreeNode("+")
root.left = TreeNode("3")
root.right = TreeNode("*")
root.right.left = TreeNode("+")
root.right.right = TreeNode("2")
root.right.left.left = TreeNode("5")
root.right.left.right = TreeNode("9")

result = evaluate_expression(root)
print(result)  
