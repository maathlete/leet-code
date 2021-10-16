# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head #we technically don't need this
        final = current #but we do need this
        
        while current:
            
            next_node = current.next
            
            #we're going to iterate through the remaining nodes until we
            #... go through all of the remaining nodes or find a new,
            #distinct node
            
            while next_node and current.val == next_node.val: 
                
                next_node = next_node.next
            
            current.next = next_node #if we found a distinct node before the LL ends, we assign it here; otherwise, this will be None
            current = current.next #adjust the current pointer to point to the new node. If this is none, the while loop will break. Otherwise, it will continue on.
        
        return(final)
