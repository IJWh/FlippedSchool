# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zzrows = []
        
        if numRows == 1:
            return s
        
        for _ in range(0,numRows):
            zzrows.append([])
        loc = 0
        down = True
        for i in s:
            zzrows[loc].append(i)
            if down:
                loc += 1
            else:
                loc -= 1
            if loc == numRows:
                down = not down
                loc -= 2
            elif loc == -1:
                down = not down
                loc += 2
        
        result_str = ''
        for zzrow in zzrows:
            for j in zzrow:
                result_str += j
        return result_str
