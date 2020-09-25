# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(pow(2,len(nums))):
            bit = "{0:b}".format(i).zfill(len(nums))
            tmp = []
            for i in range(len(nums)):
                if bit[i] == "1":
                    tmp.append(nums[i])
            result += [tmp]
            
        return result
