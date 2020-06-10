# https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        garden = defaultdict(list)
        for a, b in paths:
            garden[a].append(b)
            garden[b].append(a)
        flower = [1]* (N+1)
        
        flower[1]=1
        
        for i in garden:
            available = [1,2,3,4]
            for j in garden[i]:
                if flower[j] != 0 and flower[j] in available:
                    available.remove(flower[j])
            flower[i] = available[0]
        
        
        return flower[1:]
