# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        dif_list = []

        # 두 string간 차이를 저장하는 리스트 생성
        for i in range(len(s)):
            dif_list.append(abs(ord(s[i]) - ord(t[i])))

        # # 끝났음을 표시
        # dif_list.append(maxCost+1)
        cur_cost = 0
        max_len = 0
        start, end = 0, 0

        while start < len(dif_list) and end < len(dif_list):
            # start > end가 되는것 방지
            # end = max(start, end)
            if end < start:
                end = start
                cur_cost = 0

            # cost 계산
            if cur_cost + dif_list[end] > maxCost:
                cur_cost -= dif_list[start]
                start += 1

            else:
                cur_cost += dif_list[end]
                end += 1

                # 현재 확인된 substring의 길이와 기존 최대 길이 비교 / 갱신
                max_len = max(max_len, end - start)

        return max_len
