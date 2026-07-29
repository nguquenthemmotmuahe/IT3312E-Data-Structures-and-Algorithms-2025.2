class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftmost_child = None
        self.right_sibling = None


def findNode(root, v):
    if root is None:
        return None

    if root.data == v:
        return root

    p = root.leftmost_child

    while p is not None:
        result = findNode(p, v)

        if result is not None:
            return result

        p = p.right_sibling

    return None
    
def addFirstChild(parent_node, v):
    if parent_node is None:
        return None

    new_node = TreeNode(v)

    new_node.right_sibling = parent_node.leftmost_child
    parent_node.leftmost_child = new_node

    return new_node

def countNodes(root):
    # Count the number of nodes in the tree rooted at root.

    # Parameter:
    #    root: a reference to a TreeNode object.
    #          It is not the key/value stored in the node.

    # Return:
    #    The number of nodes in the subtree whose root node is root.
    #    If root is None, return 0.
    
    # to do by student
    if root is None:
        return 0
    
    count = 1 
    child = root.leftmost_child
    
    while child is not None:
        count += countNodes(child)
        child = child.right_sibling
        
    return count
  
def countLeaves(root):
    # Count the number of leaf nodes in the tree rooted at root.
    # Parameter:
    #      root: a reference to a TreeNode object.
    #           It is not the key/value stored in the node.

    # Return:
     #   The number of leaf nodes in the subtree whose root node is root.
     #   If root is None, return 0.

    # to do by student
    if root is None:
        return 0
        
    if root.leftmost_child is None:
        return 1
        
    leaves_count = 0
    child = root.leftmost_child
    
    while child is not None:
        leaves_count += countLeaves(child)
        child = child.right_sibling
        
    return leaves_count
  
def countChildren(node):
    # Count the number of direct children of a node.

    # Parameter:
    #    node: a reference to a TreeNode object.
    #          It is not the key/value stored in the node.

    # Return:
    #    The number of direct children of node.
    #    If node is None, return 0.
    # to do by student
    if node is None:
        return 0
        
    children_count = 0
    child = node.leftmost_child
    
    while child is not None:
        children_count += 1
        child = child.right_sibling
        
    return children_count
  
def solve():
    root = None

    while True:
        parts = input().split()

        if len(parts) == 0:
            continue

        cmd = parts[0]

        if cmd == "#":
            break

        cmd = cmd.lower()

        if cmd == "makeroot":
            x = parts[1]

            if root is None:
                root = TreeNode(x)

        elif cmd == "addfirstchild":
            x = parts[1]
            y = parts[2]

            parent_node = findNode(root, x)

            # Assume all node values are unique
            if parent_node is not None and findNode(root, y) is None:
                addFirstChild(parent_node, y)

        elif cmd == "countnodes":
            if len(parts) == 1:
                print(countNodes(root))
            else:
                x = parts[1]
                node = findNode(root, x)
                print(countNodes(node))

        elif cmd == "countleaves":
            if len(parts) == 1:
                print(countLeaves(root))
            else:
                x = parts[1]
                node = findNode(root, x)
                print(countLeaves(node))

        elif cmd == "countchildren":
            x = parts[1]
            node = findNode(root, x)
            print(countChildren(node))

solve()
