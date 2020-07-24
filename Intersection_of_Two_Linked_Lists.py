# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A_iter = headA
        B_iter = headB
        A_total = 0
        B_total = 0
        
        while A_iter is not None:
            A_total += A_iter.val
            A_iter = A_iter.next
            
            
        while B_iter is not None:
            B_total += B_iter.val
            B_iter = B_iter.next
        
        if A_iter is not B_iter:
            return None
        
        A_iter = headA
        B_iter = headB
        
        while A_iter is not B_iter:
            if A_total > B_total:
                A_total -= A_iter.val
                A_iter = A_iter.next
            else:
                B_total -= B_iter.val
                B_iter = B_iter.next
        
        return A_iter
