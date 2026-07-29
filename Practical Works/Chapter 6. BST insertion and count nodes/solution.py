class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    # Return the root node of the updated BST after inserting key.
    # If key already exists in the BST, the tree remains unchanged.
    # to do by student
    if root is None:
        return Node(key)
        
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
        
    return root

def get_size(n):
    if n is None:
        return 0
    return 1 + get_size(n.left) + get_size(n.right)
  
def count(node):
    # return  left_count: number of nodes in the left subtree of node
    # and right_count: number of nodes in the right subtree of node
    # to do by student
    if node is None:
        return 0, 0
        
    left_count = get_size(node.left)
    right_count = get_size(node.right)
    
    return left_count, right_count
  
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    root = None

    for x in arr:
        root = insert(root, x)

    left_count, right_count = count(root)

    print(left_count, right_count)


main()
