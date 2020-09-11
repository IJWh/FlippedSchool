# https://leetcode.com/problems/unique-binary-search-trees/

#	      1 
#	    (2~4)
#                   2            3             4
#                 (3~4)        1  4    (2~3)


#	          2
#        1	    (3~4)

#	           3
#      (1~2)     4

#	           4
#    (1~3)





#n=5
#		                   3
#              (1~2)	      (3~4)

class Solution:
    def numTrees(self, n: int) -> int:
        record_box = [-1] * 20
        record_box[1] = 1
        # record_box[2] = 2
        # record_box[3] = 5

        def bfs_case(start, end):
            if start >= end:
                return 1

            cnt = 0
            # 기존 결과가 저장되어있지 않다면 계산 진행
            if record_box[end - start + 1] == -1:
                for i in range(start, end + 1):
                    cnt += bfs_case(start, i-1) * bfs_case(i+1, end)
                record_box[end - start + 1] = cnt
                
            return record_box[end - start + 1]

        return bfs_case(1, n)


