#question: https://leetcode.com/problems/odd-even-linked-list/description/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        odd = ListNode(0)
        even = ListNode(0)

        odd_head = odd
        even_head = even

        i = 1

        while head:

            if i % 2 == 0:

                even.next = ListNode(head.val)
                even = even.next
            
            else:

                odd.next = ListNode(head.val)
                odd = odd.next

            head = head.next
            i += 1

        odd.next = even_head.next

        return(odd_head.next)
