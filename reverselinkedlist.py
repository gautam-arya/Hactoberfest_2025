class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

# Helper to create and print list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


