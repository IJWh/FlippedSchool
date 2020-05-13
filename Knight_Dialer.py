# https://leetcode.com/problems/knight-dialer/submissions/
class Solution:
    def knightDialer(self, N: int) -> int:
        MOD = 1000000000 + 7
        # 0 => 4,6  1 => 6,8  2 => 7,9  3 => 4,8  4 => 0,3,9  5 => _
        # 6 => 0,1,7   7 => 2,6  8 => 1,3  9 => 2,4
        
        available_loc = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        
        dialer_digit = [1]*10
        for trier in range(N-1):
            tmp_hop = [0]*10
            for idx, cnt in enumerate(dialer_digit):
                for pre_loc in available_loc[idx]:
                    tmp_hop[pre_loc] += cnt
            dialer_digit = tmp_hop
        
        return sum(dialer_digit) %MOD
