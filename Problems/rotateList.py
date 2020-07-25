# Kamesh Vedula
# Problem: Rotate List

def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
    if not head:
        return None

    #loop thru LL and connect both ends
    # also keep track of the length of LL
    curr = head
    nodes = 1
    while curr.next:
        curr = curr.next
        nodes += 1
    curr.next = head

    #This is where you rotate at desired index
    rotate_loc = nodes - (k % nodes)
    for i in range(rotate_loc):
        curr = curr.next
                         
    prev = curr        
    curr = curr.next
    prev.next = None
    return curr