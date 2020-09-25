# https://leetcode.com/problems/bitwise-and-of-numbers-range/
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        checker = pow(2,31)-1
        # (5,8)의 경우에는 계산중 8(1000)을 건너뜀 > 바뀌는 자릿수에 대한 연산 불가
        result = m & n
        # 시간제한
        while m <= n:
            result &= m
            
            # 다음에 연산할 값 계산
            tmp = "{0:b}".format(checker & result)
            first_one = tmp.rsplit('1',1)[-1]
            m += pow(2,len(first_one))
            
            # 결과값이 0이라면 이 이상 계산은 의미 없음
            if not result:
                break
        return result
