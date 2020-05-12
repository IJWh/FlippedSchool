# https://leetcode.com/problems/unique-paths/submissions/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_cnt = []
        for i in range(0,min(n,m)):
            path_cnt.append(1)
        for i in range(1,max(n,m)):
            for j in range(1,min(n,m)):
                path_cnt[j] += path_cnt[j-1]

                
        
        return path_cnt[-1]
