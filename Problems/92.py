# Kamesh Vedula
# Problem: Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    dummy = dummy_head = ListNode()
    dummy.next = head
    
    for _ in range(m - 1):
        dummy = dummy.next
        
    itr = dummy.next  
    
    for _ in range(n - m):
        temp = itr.next
        dummy.next, temp.next, itr.next = temp, dummy.next, temp.next
        
    return dummy_head.next

