# https://leetcode.com/problems/add-two-numbers/

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 좌표에서 원점으로부터의 거리 추출, 해당 index도 같이 저장
        point_dist = list([points[i][0]**2 + points[i][1]**2, i] for i in range(len(points)))
        # 해당 리스트 정렬
        point_dist = sorted(point_dist)
        # 정렬한 리스트를 앞에서부터 K번째까지만, 그 거리의 index값을 추출
        target_idx = list(i[1] for i in point_dist[:K])
        # 추출한 index값으로 points 리스트로부터 해당 좌표를 추출
        return list(points[i] for i in target_idx)
        
        # return list(points[i] for i in list(i[1] for i in sorted(list([points[i][0]**2 + points[i][1]**2, i] for i in range(len(points))))[:K]))
