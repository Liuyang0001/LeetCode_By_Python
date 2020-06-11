#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01-matrix
#
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        que = []
        row, col = len(matrix),len(matrix[0])
        res = [[-1]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if not matrix[i][j]:
                    que.append((i, j))
                    res[i][j] = 0
        depth = 0
        offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while que:
            depth += 1
            tmp = []
            for i, j in que: # 更新每个点周围的4个点
                for x_offset, y_offset in offset:
                    x, y = i+x_offset, j+y_offset
                    # 新探索的有效点
                    if 0<=x<row and 0<=y<col and res[x][y]<0: 
                        res[x][y] = depth
                        tmp.append((x, y))
            que = tmp
        return res
# @lc code=end