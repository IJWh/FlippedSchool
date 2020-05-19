# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = S[0]
        
        for i in S[1:]:
            if len(result) == 0 or result[-1] != i:
                result +=i
            else:
                result = result[:-1]
        
        return result
                
            
