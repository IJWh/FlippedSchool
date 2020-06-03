# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 1_000_000_000 + 7
        if target < d:
            return 0
        
        default_cnt = []
        for i in range(target+1):
            default_cnt.append([0 for _ in range(f+1)])
        
        # first dice
        current_cnt = copy.deepcopy(default_cnt)
        for i in range(1,min(f,target)+1):
            current_cnt[i][i] = 1
        
        num = 2
        for k in range(1,d):
            tmp_cnt = copy.deepcopy(default_cnt)
            for i in range(num, min(f*(k+1),target)+1):
                for j in range(1,f+1):
                    tmp_cnt[i][j] = sum(current_cnt[i-j]) if i-j > 0 else 0
            current_cnt = tmp_cnt
            num += 1
            
        return sum(current_cnt[target]) % modulo


# target = 12
# dice = 2
# face = 6

# list cnt: cnt[target][face]

#    1  2  3  4  5  6  7  8  9  10  11  12  target
# 1  0  0  0  0  0  0  0  0  0   0   0    0
# 2  0  0  0  0  0  0  0  0  0   0   0    0
# 3  0  0  0  0  0  0  0  0  0   0   0    0
# 4  0  0  0  0  0  0  0  0  0   0   0    0
# 5  0  0  0  0  0  0  0  0  0   0   0    0
# 6  0  0  0  0  0  0  0  0  0   0   0    0
# face
# =====================
# =====================
# d = 1
#    1  2  3  4  5  6  7  8  9  10  11  12  target
# 1  1  0  0  0  0  0  0  0  0   0   0    0
# 2  0  1  0  0  0  0  0  0  0   0   0    0
# 3  0  0  1  0  0  0  0  0  0   0   0    0
# 4  0  0  0  1  0  0  0  0  0   0   0    0
# 5  0  0  0  0  1  0  0  0  0   0   0    0
# 6  0  0  0  0  0  1  0  0  0   0   0    0
# face
# ==========================================
# d= 2

#    1  2  3  4  5  6  7  8  9  10  11  12  target
# 1  0  1  1  1  1  1  1  0  0   0   0    0
# 2  0  0  1  1  1  1  1  1  0   0   0    0
# 3  0  0  0  1  1  1  1  1  1   0   0    0
# 4  0  0  0  0  1  1  1  1  1   1   0    0
# 5  0  0  0  0  0  1  1  1  1   1   1    0
# 6  0  0  0  0  0  0  1  1  1   1   1    1
# face
# ===========================================
# d=3                                        (t)
#    1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18
# 1  0  0  1  2  3  4  5  6  5   4   3    2    1   0   0    0    0    0
# 2  0  0  0  1  2  3  4  5  6   5   4    3    2   1   0    0    0    0
# 3  0  0  0  0  1  2  3  4  5   6   5    4    3   2   1    0    0    0
# 4  0  0  0  0  0  1  2  3  4   5   6    5    4   3   2    1    0    0
# 5  0  0  0  0  0  0  1  2  3   4   5    6    5   4   3    2    1    0
# 6  0  0  0  0  0  0  0  1  2   3   4    5    6   5   4    3    2    1
# face

# cnt[target][face]
# face = 주사위를 던져서 나온 값
# target = 다 더했을때 나와야 하는 값

# d(n)일때의 cnt[target][face] = d(n-1)에서의 sum(cnt[target-face][1~face])


# target = 2+3+4+5+6+5 = 25
