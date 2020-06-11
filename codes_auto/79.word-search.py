#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] word-search
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def __dfs(i, j, wd_len, visited):
            if wd_len == len(word):
                return True
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tem_i = x + i
                tem_j = y + j
                if 0 <= tem_i < row and 0 <= tem_j < col and board[tem_i][tem_j] == word[wd_len] \
                                                       and (tem_i, tem_j) not in visited:
                    visited.add((tem_i, tem_j))
                    if __dfs(tem_i, tem_j, wd_len+1, visited):
                        return True
                    visited.remove((tem_i, tem_j))
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and __dfs(i, j, 1, {(i, j)}):
                    return True
        return False
# @lc code=end