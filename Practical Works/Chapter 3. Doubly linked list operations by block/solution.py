class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

head = None
tail = None

def find(head, k):
    p = head
    while p is not None:
        if p.key == k:
            return p
        p = p.next
    return None

def insert_last(head, tail, v):
    new_node = Node(v)

    if head is None:
        return new_node, new_node

    tail.next = new_node
    new_node.prev = tail
    tail = new_node
    return head, tail

def print_list(head):
    p = head
    while p is not None:
        print(p.key, end=" ")
        p = p.next
    print()

def print_reverse(tail):
    p = tail
    while p is not None:
        print(p.key, end=" ")
        p = p.prev
    print()

def remove_node(head, tail, v):
    # return head and tail of the obtained list 
    # to do by student
    p = find(head, v)
    if p is None:
        return head, tail
    if p.prev:
        p.prev.next = p.next
    else:
        head = p.next
    if p.next:
        p.next.prev = p.prev
    else:
        tail = p.prev
    return head, tail
  
def reverse(head, tail):
    # return head and tail of the obtained list after reverse
    # to do by student
    curr = head
    while curr is not None:
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev 
    head, tail = tail, head
    return head, tail
  
def add_first(head, tail, v):
    # return head and tail of the obtained list 
    # to do by student
    new_node = Node(v)
    if head is None:
        return new_node, new_node
    new_node.next = head
    head.prev = new_node
    head = new_node
    return head, tail


def add_before(head, tail, u, v):
    # return head and tail of the obtained list
    #to do by student
    v_node = find(head, v)
    if v_node is None:
        return head, tail
    new_node = Node(u)
    new_node.next = v_node
    new_node.prev = v_node.prev
    if v_node.prev:
        v_node.prev.next = new_node
    else:
        head = new_node
    v_node.prev = new_node
    return head, tail
   
def add_after(head, tail, u, v):
    # return head and tail of the obtained list
    #to do by student
    v_node = find(head, v)
    if v_node is None:
        return head, tail
    new_node = Node(u)
    new_node.prev = v_node
    new_node.next = v_node.next
    if v_node.next:
        v_node.next.prev = new_node
    else:
        tail = new_node
    v_node.next = new_node
    return head, tail
  
def solve():
    global head, tail

    n = int(input())
    arr = list(map(int, input().split()))

    for k in arr:
        head, tail = insert_last(head, tail, k)

    while True:
        parts = input().split()
        cmd = parts[0]

        if cmd == "#":
            break

        if cmd == "addlast":
            k = int(parts[1])
            if find(head, k) is None:
                head, tail = insert_last(head, tail, k)

        elif cmd == "addfirst":
            k = int(parts[1])
            if find(head, k) is None:
                head, tail = add_first(head, tail, k)

        elif cmd == "addafter":
            u = int(parts[1])
            v = int(parts[2])
            if find(head, u) is None:
                head, tail = add_after(head, tail, u, v)

        elif cmd == "addbefore":
            u = int(parts[1])
            v = int(parts[2])
            if find(head, u) is None:
                head, tail = add_before(head, tail, u, v)

        elif cmd == "remove":
            k = int(parts[1])
            head, tail = remove_node(head, tail, k)

        elif cmd == "reverse":
            head, tail = reverse(head, tail)


solve()
print_list(head)
print_reverse(tail)
