# https://leetcode.com/problems/can-i-win/
# https://leetcode.com/problems/can-i-win/discuss/591993/4-lines-Python-with-frozenset

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @functools.lru_cache(None)
        def dp(nums, left):
            return any(left - n <= 0 or not dp(frozenset(nums - {n}), left - n) for n in nums)
        
        return  (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dp(frozenset(range(1, maxChoosableInteger + 1)), desiredTotal)
