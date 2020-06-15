# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        next_rotten = []
        current_rotten = []
        minutes = 0
        
        total_fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total_fresh += 1
                elif grid[i][j] == 2:
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        next_rotten.append([i-1,j])
                    if i + 1 < len(grid) and grid[i+1][j] == 1:
                        next_rotten.append([i+1,j])
                    if j -1 >= 0 and grid[i][j-1] == 1:
                        next_rotten.append([i,j-1])
                    if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                        next_rotten.append([i,j+1])
        
        while len(next_rotten) > 0:
            current_rotten = next_rotten
            next_rotten = []
            new_rotten = False
            
            for i,j in current_rotten:
                if grid[i][j] == 2:
                    continue
                grid[i][j] = 2
                total_fresh -= 1
                new_rotten = True
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    next_rotten.append([i-1,j])
                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    next_rotten.append([i+1,j])
                if j -1 >= 0 and grid[i][j-1] == 1:
                    next_rotten.append([i,j-1])
                if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                    next_rotten.append([i,j+1])
                
            if new_rotten:
                minutes += 1
        
        
        
        if total_fresh > 0:
            return -1
        else:
            return minutes
