# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         comp_num = 1
#         diag_idx = 0
#         while k > comp_num:
#             k -= comp_num
#             diag_idx += 1
#             comp_num = comp_num + 1 if diag_idx < len(matrix) else comp_num-1

#         if diag_idx < len(matrix):
#             r_idx, c_idx = diag_idx, 0
#         else:
#             r_idx = len(matrix) -1 
#             c_idx = diag_idx - r_idx

#         comp_list = list(matrix[r_idx - i][c_idx + i] for i in range(comp_num))
#         comp_list = sorted(comp_list)
#         return comp_list[k-1]
        comp_list = []
        
        for i in matrix:
            comp_list += i
            
        comp_list = sorted(comp_list)

        return comp_list[k-1]
