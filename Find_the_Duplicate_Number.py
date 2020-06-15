# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         range_sum = 0
#         list_sum = 0
#         max_num = 1
        
#         for i in nums:
#             list_sum += i
#             max_num = max(max_num,i)
            
#         for i in range(1,max_num+1):
#             range_sum += i
            
#         return list_sum - range_sum
        nums_dict = {}
        
        for i in nums:
            if i in nums_dict.keys():
                return i
            else:
                nums_dict[i] = 1
