# https://leetcode.com/problems/intersection-of-two-arrays/
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        num = [-1]* (max(max(nums1),max(nums2))+1)
        for i in nums1:
            num[i] = 0
            
        for i in nums2:
            if num[i] == 0:
                num[i] = 1 
        
        result = []
        for i in range(len(num)):
            if num[i] == 1:
                result.append(i)
                
        return result
