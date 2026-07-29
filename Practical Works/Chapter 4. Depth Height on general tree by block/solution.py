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


def heightNode(p):
    # Compute the height of the subtree rooted at node p.

    # Parameter:
    #    p: a reference to a TreeNode object.
    #       It is not the key/value stored in the node.

    # Return:
    #    The height of the subtree rooted at p.
    #    If p is None, return 0.

    # Note: the height of a leaf node is 1.
    
    # to do by student
    if p is None:
        return 0
    
    max_child_height = 0
    child = p.leftmost_child
    
    while child is not None:
        h = heightNode(child)
        if h > max_child_height:
            max_child_height = h
        child = child.right_sibling
        
    return max_child_height + 1
  
def depth(r, v, d=1):
    # Compute the depth of the node whose value is v in the tree rooted at r.

    # Parameters:
    #    r: a reference to a TreeNode object.
    #       It is not the key/value stored in the node.

    #    v: the key/value to search for.

    #    d: the current depth of node r.
    #       The default value is 1 because the root has depth 1.

    # Return:
    #    The depth of the node whose data is equal to v.
    #    If v is not found, return -1.

    # to do by student
    if r is None:
        return -1
    
    if r.data == v:
        return d
        
    child_depth = depth(r.leftmost_child, v, d + 1)
    if child_depth != -1:
        return child_depth
        
    return depth(r.right_sibling, v, d)
  
def degreeOfTree(root):
    #Compute the degree of the tree rooted at root.

    #Parameter:
    #    root: a reference to a TreeNode object.
    #          It is not the key/value stored in the node.

    #Return:
    #    The maximum number of children of any node in the subtree rooted at root.
    #    If root is None, return 0.
  
    # to do by student
    if root is None:
        return 0
        
    children_count = 0
    child = root.leftmost_child
    
    while child is not None:
        children_count += 1
        child = child.right_sibling
        
    return max(children_count, 
               degreeOfTree(root.leftmost_child), 
               degreeOfTree(root.right_sibling))
  
def areSiblings(u, v, root):
    # Check whether two nodes u and v are siblings in the tree rooted at root.

    # Parameters:
    #    u: a reference to a TreeNode object.
    #    v: a reference to a TreeNode object.
    #    root: a reference to the root TreeNode object of the tree.

    # Return:
    #    True if u and v have the same parent.
    #    Otherwise, return False.
  
    # to do by student
    if root is None or u is None or v is None:
        return False
        
    has_u = False
    has_v = False
    
    child = root.leftmost_child
    while child is not None:
        if child.data == u.data:
            has_u = True
        if child.data == v.data:
            has_v = True
        child = child.right_sibling
        
    if has_u and has_v:
        return True
        
    return areSiblings(u, v, root.leftmost_child) or areSiblings(u, v, root.right_sibling)
  
def solve():
    root = None

    while True:
        try:
            parts = input().split()
        except EOFError:
            break

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

            if parent_node is not None and findNode(root, y) is None:
                addFirstChild(parent_node, y)

        elif cmd == "findnode":
            x = parts[1]

            node = findNode(root, x)

            if node is None:
                print(0)
            else:
                print(1)

        elif cmd == "heightnode":
            x = parts[1]

            node = findNode(root, x)

            print(heightNode(node))

        elif cmd == "depth":
            x = parts[1]

            print(depth(root, x))

        elif cmd == "degreeoftree":
            if len(parts) == 1:
                print(degreeOfTree(root))
            else:
                x = parts[1]
                node = findNode(root, x)
                print(degreeOfTree(node))

        elif cmd == "aresiblings":
            x = parts[1]
            y = parts[2]

            u = findNode(root, x)
            v = findNode(root, y)

            if areSiblings(u, v, root):
                print(1)
            else:
                print(0)


solve()
