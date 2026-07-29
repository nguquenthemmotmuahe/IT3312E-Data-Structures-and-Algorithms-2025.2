import sys

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
  
def preorder(root, result):
    # Result: a list used to store the keys visited during the pre-order traversal.
    # to do by student
    if root is None:
        return
        
    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)
  
def main():
    root = None

    for line in sys.stdin:
        line = line.strip()

        if line == "#":
            break

        parts = line.split()

        if parts[0] == "insert":
            key = int(parts[1])
            root = insert(root, key)

    result = []
    preorder(root, result)

    print(" ".join(result))


if __name__ == "__main__":
    main()
