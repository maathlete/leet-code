# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:41:23 2021

@author: aaaro
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import ListNode

class Solution:
    def reverseList(self, head):
        
        current = head
        previous = None
        
        while current:
            
            remaining = current.next
            current.next = previous
            previous = current
            current = remaining
            
        head = previous
        return(head)
        
            
            
            
            
        