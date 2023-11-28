from collections import deque

class Node:

    def __init__(self, val: int = 0) -> None:
        self.val  = val
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, root, val):
        if root == None:
            return Node(val)
        else:
            if root.val < val:
                root.right = self.insert(root.right, val)
            else:
                root.left = self.insert(root.left, val)
        return root
    
    def insert_to_tree(self, root, val):
        self.root = self.insert(root, val)

    def print_binary_tree_recursive(self, node):
        if node == None:
            return
        self.print_binary_tree_recursive(node.left)
        print(node.val)
        self.print_binary_tree_recursive(node.right)

    def print_binary_tree(self, root):
        if root == None:
            return
        stack = deque()
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            print(cur.val)
            cur = cur.right



if __name__ == "__main__":
    arr = [10, 4, 3, 2, 6, 15, 12, 11, 20]
    tree = BinaryTree()
    print(tree)
    for x in arr:
        tree.insert_to_tree(tree.root, x)
    tree.print_binary_tree_recursive(tree.root)
    tree.print_binary_tree(tree.root)
    
