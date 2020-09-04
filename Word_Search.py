# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        self.row_max = len(board)
        self.col_max = len(board[0])

        def dfs(row, col, matching_idx):
            # 현 좌표의 글자가 검사 대상과 일치하는가
            if board[row][col] != word[matching_idx]:
                return

            # 끝까지 매칭 되었는가
            if matching_idx == len(word)-1:
                self.result = True
                return

            # 사용된 문자의 중복사용 방지
            board[row][col] = str(matching_idx)

            if not self.result and row - 1 >= 0:
                dfs(row - 1, col, matching_idx+1)
            if not self.result and row + 1 < self.row_max:
                dfs(row + 1, col, matching_idx+1)
            if not self.result and col - 1 >= 0:
                dfs(row, col - 1, matching_idx+1)
            if not self.result and col + 1 < self.col_max:
                dfs(row, col + 1, matching_idx+1)

            # 문자 원복
            board[row][col] = word[matching_idx]
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                # 첫 글자 매칭 확인
                if board[i][j] == word[0]:
                    dfs(i, j, 0)

        return self.result
