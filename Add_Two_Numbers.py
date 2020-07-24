# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #num1 = 0
        #num2 = 0
        
        #idx = 0
        #l_iter = l1
        #while l_iter is not None:
        #    num1 += l_iter.val * 10 ** idx
        #    l_iter = l_iter.next
        #    idx += 1
            
        #idx = 0
        #l_iter = l2
        #while l_iter is not None:
        #    num2 += l_iter.val * 10 ** idx
        #    l_iter = l_iter.next
        #    idx += 1
            
        #final_num = num1+num2
        
        #result = ListNode(final_num % 10)
        #final_num = int(final_num/10)
        #r_iter = result
        #while final_num > 0:
        #    r_iter.next = ListNode(final_num % 10)
        #    r_iter = r_iter.next
        #    final_num = int(final_num/10)
            
        #return result
        l1_iter = l1
        l2_iter = l2
        sum_val = l1_iter.val + l2_iter.val
        add = 1 if sum_val >= 10 else 0
        sum_val %= 10
        result = ListNode(sum_val)
        
        r_iter = result
        l1_iter = l1_iter.next
        l2_iter = l2_iter.next
        
        while l1_iter is not None and l2_iter is not None:
            sum_val = l1_iter.val + l2_iter.val + add
            add = 1 if sum_val >= 10 else 0
            sum_val %= 10
            r_iter.next = ListNode(sum_val)
            r_iter = r_iter.next
            
            l1_iter = l1_iter.next
            l2_iter = l2_iter.next
            
        if l1_iter is None:
            while l2_iter is not None:
                sum_val = l2_iter.val + add
                add = 1 if sum_val >= 10 else 0
                sum_val %= 10
                r_iter.next = ListNode(sum_val)
                l2_iter = l2_iter.next
                r_iter = r_iter.next
        else:
            while l1_iter is not None:
                sum_val = l1_iter.val + add
                add = 1 if sum_val >= 10 else 0
                sum_val %= 10
                r_iter.next = ListNode(sum_val)
                l1_iter = l1_iter.next
                r_iter = r_iter.next
        
        if add == 1:
            r_iter.next = ListNode(add)
        
        return result
