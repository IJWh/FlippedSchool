# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bi_search(left, right ):
            mid = int((left + right) / 2)
            
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] == target:
                return mid
            elif left >= right:
                return -1
            elif nums[mid] < target:
                return bi_search(mid+1, right-1)
            else:
                return bi_search(left+1, mid-1)
        
        if len(nums) == 0:
            return [-1,-1]
        
        detected = bi_search(0,len(nums)-1)
        start = detected
        end = detected
        
        while start >= 0:
            if start >= 1 and nums[start-1] == target:
                start -= 1
            else:
                break
        
        while end < len(nums):
            if end <= len(nums)-2 and nums[end+1] == target:
                end += 1
            else:
                break

        return [start,end]
