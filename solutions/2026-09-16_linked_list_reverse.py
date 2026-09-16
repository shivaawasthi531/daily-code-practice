"""
Reverse a singly linked list
Auto-generated daily practice solution.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    new_head = reverse_list(head)
    out = []
    while new_head:
        out.append(new_head.val)
        new_head = new_head.next
    print(out)  # [3, 2, 1]
