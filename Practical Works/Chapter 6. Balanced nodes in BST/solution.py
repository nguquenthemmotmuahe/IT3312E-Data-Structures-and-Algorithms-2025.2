import sys
sys.setrecursionlimit(3000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

ans = 0

def dfs(node):
    global ans
    if not node:
        return 0
    l = dfs(node.left)
    r = dfs(node.right)
    if (node.left or node.right) and l == r:
        ans += 1
    return l + r + 1

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    root = None
    for i in range(1, n + 1):
        root = insert(root, int(data[i]))
    
    dfs(root)
    print(ans)
