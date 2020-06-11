#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] valid-sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_ls = [{} for i in range(9)]
        columns_ls = [{} for i in range(9)]
        boxes_ls = [{} for i in range(9)]
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num != ".":
                    num = int(num)
                    box_index = row//3*3+column//3
                    rows_ls[row][num] = rows_ls[row].get(num, 0) + 1
                    columns_ls[column][num] = columns_ls[column].get(
                        num, 0) + 1
                    boxes_ls[box_index][num] = boxes_ls[box_index].get(
                        num, 0) + 1

                    # check valid
                    if rows_ls[row][num] > 1 or columns_ls[column][num] > 1 or boxes_ls[box_index][num] > 1:
                        return False
        return True
# @lc code=end