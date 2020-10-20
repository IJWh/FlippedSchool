# https://leetcode.com/problems/decode-ways/
# O(N)/O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        dynamic_result = [0]*(len(s) +1)
        dynamic_result[0] = 1
        dynamic_result[1] = 1 if s[0] != '0' else 0
        for s_idx in range(2, len(s)+1):
            if s[s_idx -1] != "0":
                dynamic_result[s_idx] += dynamic_result[s_idx-1]
            # if 0<=  int(s[s_idx-1]) < 7 and s[s_idx -2] in ["0","1","2"]:
            duo = int(s[s_idx-2:s_idx])
            if 10<= duo <= 26:
                dynamic_result[s_idx] += dynamic_result[s_idx -2]
            
            
        
        return dynamic_result[len(s)]
