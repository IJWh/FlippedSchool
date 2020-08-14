# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m_intervals = []
        if not intervals:
            return m_intervals

        intervals = sorted(intervals)
        
        s_idx, e_idx = 0,1
        tmp = [intervals[0][0],intervals[0][1]]

        for i in intervals:
            if i[0] <= tmp[1]:
                tmp[1] = max(tmp[1],i[1])
            else:
                m_intervals.append(tmp)
                tmp = copy.deepcopy(i)
        
        if not m_intervals or tmp[1] != m_intervals[-1][1]:
            m_intervals.append(tmp)
            
        return m_intervals
