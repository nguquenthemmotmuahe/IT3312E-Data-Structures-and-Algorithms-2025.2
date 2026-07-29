import sys
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

nodes = {}

def is_max_heap(node):
    if not node:
        return True
    if node.left and node.left.id >= node.id:
        return False
    if node.right and node.right.id >= node.id:
        return False
    return is_max_heap(node.left) and is_max_heap(node.right)

def count_2_children(node):
    if not node:
        return 0
    ans = 1 if node.left and node.right else 0
    return ans + count_2_children(node.left) + count_2_children(node.right)

data = sys.stdin.read().split()
if not data:
    sys.exit()

i = 0
while data[i] != '*':
    cmd = data[i]
    if cmd == 'make-root':
        u = int(data[i+1])
        nodes[u] = Node(u)
        i += 2
    elif cmd == 'add-left':
        u = int(data[i+1])
        v = int(data[i+2])
        if v in nodes and u not in nodes and not nodes[v].left:
            nodes[u] = Node(u)
            nodes[v].left = nodes[u]
        i += 3
    elif cmd == 'add-right':
        u = int(data[i+1])
        v = int(data[i+2])
        if v in nodes and u not in nodes and not nodes[v].right:
            nodes[u] = Node(u)
            nodes[v].right = nodes[u]
        i += 3

i += 1
while i < len(data) and data[i] != '***':
    cmd = data[i]
    u = int(data[i+1])
    if cmd == 'is-max-heap':
        if u not in nodes:
            print(1)
        else:
            print(1 if is_max_heap(nodes[u]) else 0)
    elif cmd == 'count-nodes-having-2-children':
        if u not in nodes:
            print(0)
        else:
            print(count_2_children(nodes[u]))
    i += 2
