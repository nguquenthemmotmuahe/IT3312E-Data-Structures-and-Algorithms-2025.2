class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
        

def insert_to_head(head, value):
    # to do by student: Write down your code here
    new_node = Node(value)
    new_node.next = head
    return new_node
  
# Main program
n = int(input())
numbers = list(map(int, input().split()))

head = None
for x in numbers:
    head = insert_to_head(head, x)

print_list(head)

