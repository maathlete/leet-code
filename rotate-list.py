# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or k == 0:
            return(head)
        
        vals = []
        
        current = head
        
        while current:
            
            vals.append(current.val)
            current = current.next
            
        if k % len(vals) == 0:
            return(head)
        
        else: 
            k = k % len(vals)
            
            for i in range(k):

                new = [vals[-1]]
                vals = new + vals[:-1]

            final = ListNode(vals[0])
            ptr = final

            for i in vals[1:]:

                final.next = ListNode(i)
                final = final.next

            return(ptr)
            
