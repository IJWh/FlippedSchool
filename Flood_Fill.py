# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        max_row = len(image)
        max_col = len(image[0])

        def spread(r: int, c: int):
            nonlocal max_row
            nonlocal max_col

            oldColor, image[r][c] = image[r][c], newColor

            if r - 1 >= 0 and image[r - 1][c] == oldColor:
                spread(r-1,c)
            if c - 1 >= 0 and image[r][c - 1] == oldColor:
                spread(r, c-1)
            if r + 1 < max_row and image[r + 1][c] == oldColor:
                spread(r + 1, c)
            if c + 1 < max_col and image[r][c + 1] == oldColor:
                spread(r, c+1)
            return
        spread(sr, sc)
        return image
