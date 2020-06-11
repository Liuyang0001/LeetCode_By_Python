#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] game-of-life
#
from copy import deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        offset = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        # board_copy = [[board[r][c]
        #         for c in range(col)]
        #             for r in range(row)]
        board_copy = deepcopy(board)
        # print(board_copy)

        def judge(board,x, y) -> int:
            live, die = 0, 0
            cur = board[x][y]
            for x_off, y_off in offset:
                i = x + x_off
                j = y + y_off
                if not (0 <= i < row and 0 <= j < col):
                    continue
                if board[i][j] == 1: live += 1
                else: die += 1
            if cur == 1:
                if live < 2 or live > 3: return 0
                else: return 1
            elif cur == 0 and live == 3:
                return 1
            else: return cur  # 不发生变化
        
        # 遍历更改
        for i in range(row):
            for j in range(col):
                board[i][j] = judge(board_copy, i, j)
        
            
            
# @lc code=end