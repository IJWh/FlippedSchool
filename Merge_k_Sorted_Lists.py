# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        num_dict = {}

        for i in lists:
            head = i
            while head:
                if head.val in num_dict:
                    num_dict[head.val] += 1
                else:
                    num_dict[head.val] = 1
                head = head.next

        if not num_dict:
            return None
        
        num_dict = dict(sorted(num_dict.items()))

        m_list = ListNode(val = next(iter(num_dict)))
        num_dict[m_list.val] -= 1
        m_head = m_list
        for i in num_dict:
            while num_dict[i] > 0:
                m_head.next = ListNode(val=i)
                m_head = m_head.next
                num_dict[i] -= 1
        return m_list
