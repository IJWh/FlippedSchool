# https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        # result_mat = [[0]*n]*m
        # 이렇게 2차원 배열을 만들경우 한번의 수정으로 같은 열들이 동시에 업데이트가 된다
        result_mat = []
        for i in range(m):
            result_mat.append([0]*n)
        
        for i in range(m):
            for j in range(n):
                result_mat[i][j] = sum([sum(mat[k][max(0,j-K):min(n,j+K+1)]) for k in range(max(0,i-K),min(m,i+K+1))])
        
        return result_mat
