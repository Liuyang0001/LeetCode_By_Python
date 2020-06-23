#
# @lc app=leetcode.cn id=100261 lang=python3
#
# [100261] tic-tac-toe-lcci
#
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        N = len(board)
        self.Pending = False
        row_X,row_O,col_X,col_O = [0]*N,[0]*N,[0]*N,[0]*N
        corner_X,corner_O = [0]*2,[0]*2
        # 遍历
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'X':
                    row_X[i] += 1
                    col_X[j] += 1
                    if i==j:
                        corner_X[0]+=1
                    if i+j == N-1:
                        corner_X[1]+=1
                elif board[i][j] == 'O':
                    row_O[i] += 1
                    col_O[j] += 1
                    if i==j:
                        corner_O[0]+=1
                    if i+j == N-1:
                        corner_O[1]+=1
                elif board[i][j]==" ":
                    self.Pending = True
        print(row_X,row_O,col_X,col_O)
        if N in row_O or N in col_O or N in corner_O: return "O"
        elif N in row_X or N in col_X or N in corner_X: return "X"
        return "Pending" if self.Pending else "Draw"

# @lc code=end