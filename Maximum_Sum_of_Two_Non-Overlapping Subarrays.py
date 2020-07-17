# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        """
        result_list = [sum(A[:L+M]), sum(A[-1*(L+M):])]
        
        
        # L 중심
        l_sum_list = []
        m_sum_list = []
        result = 0
        for start_idx in range(len(A)-L+1):
            sum_sub = sum(A[start_idx:start_idx + L])
            l_sum_list.append(sum_sub)
            
        max_sum_idx = l_sum_list.index(max(l_sum_list))
        result = l_sum_list[max_sum_idx]
        
        for start_idx in range(0, max_sum_idx - M + 1):
            sum_sub = sum(A[start_idx:start_idx + M])
            m_sum_list.append(sum_sub)
            
        for start_idx in range(max_sum_idx+L, len(A) - M + 1):
            sum_sub = sum(A[start_idx:start_idx + M])
            m_sum_list.append(sum_sub)
        
        if len(m_sum_list) > 0:
            result += max(m_sum_list)
            result_list.append(result)
        
        # M 중심
        l_sum_list = []
        m_sum_list = []
        result = 0
        for start_idx in range(len(A)-M+1):
            sum_sub = sum(A[start_idx:start_idx + M])
            l_sum_list.append(sum_sub)
            
        max_sum_idx = l_sum_list.index(max(l_sum_list))
        result = l_sum_list[max_sum_idx]
        
        for start_idx in range(0, max_sum_idx - L + 1):
            sum_sub = sum(A[start_idx:start_idx + L])
            m_sum_list.append(sum_sub)
            
        for start_idx in range(max_sum_idx+M, len(A) - L + 1):
            sum_sub = sum(A[start_idx:start_idx + L])
            m_sum_list.append(sum_sub)
        
        if len(m_sum_list) > 0:
            result += max(m_sum_list)
            result_list.append(result)
        
        
        
        return max(result_list)
        """
        # 누적값으로 수정
        for i in range(1,len(A)):
            A[i] += A[i-1]
        
        result = A[L+M-1]
        Lmax = A[L-1]
        Mmax = A[M-1]
        
        for i in range(L+M, len(A)):
            Lmax = max(Lmax, A[i-M] - A[i-M-L])
            Mmax = max(Mmax, A[i-L] - A[i-M-L])
            result = max(result, Lmax + A[i] - A[i-M], Mmax + A[i] - A[i-L])
        
        return result
