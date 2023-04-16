# Define a function or write a method Fib_tree(n) in a class to create Fibonacci tree based on Fibonacci sequence, such as 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … …, and n (starting from 1) is n^th term in the series. For instance, the following two trees will be generated when Fib_tree(6) and Fib_tree(7) are invoked.

class FibTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def generate(self, n):
        if n < 1:
            return None

        if n == 1:
            return FibTree(0)
        
        if n == 2:
            return FibTree(1)
        
        left = self.generate(n - 1)
        right = self.generate(n - 2)

        node = FibTree(left.val + right.val)
        node.left = left
        node.right = right

        return node
    

fib_tree_6 = FibTree(0).generate(6)

print(fib_tree_6.val)  
print(fib_tree_6.left.val)  
print(fib_tree_6.left.left.val) 
print(fib_tree_6.left.left.left.val)  
print(fib_tree_6.left.right.val)  
print(fib_tree_6.right.val)  
print(fib_tree_6.right.left.val)  
print(fib_tree_6.right.left.left.val)  
print(fib_tree_6.right.right.val) 
print(fib_tree_6.right.right.left.val) 
print(fib_tree_6.right.right.left.left.val)  