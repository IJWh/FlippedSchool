# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        break_check = [False]*(len(s)+1)
        # 앞으로 True인 index 다음칸에 대해서만 검사를 실시할것
        # 첫번째 글자는 무조건 검사 실시
        break_check[0] = True
        
        # 글자수별로 wordDict를 나눈 dict 생성
        len_word = {}
        
        for word in wordDict:
            if len(word) not in len_word:
                len_word[len(word)] = [word]
            else:
                len_word[len(word)].append(word)
        
        # 첫번째 글자부터 순회 시작
        for idx in range(len(s)):
            if break_check[idx]:
                # next_pos = idx
                # 비교해야하는 글자수로만 비교
                for w_length in len_word:
                    if idx + w_length < len(break_check) and s[idx:idx +w_length] in len_word[w_length]:
                        break_check[idx+w_length] = True
        
        return break_check[-1]
