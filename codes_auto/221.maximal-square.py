#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] maximal-square
#
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        row,col = len(matrix), len(matrix[0])
        def bfs(x, y, k):
            # 边界，假设(0,0),边长为2，最大坐标为(1,1)
            if x + k >= row or y + k >= col:
                return k - 1
            # 边长+1 在原基础上增加两条边
            # x 的范围[x:x+k]
            for i in range(x, x + k+1):
                if matrix[i][y + k] == "0":
                    return k - 1
            for j in range(y, y + k+1):
                if matrix[x + k][j] == "0":
                    return k - 1
            # print("x,y",x,y,"增量为{}时满足".format(k))
            # 边长为k均满足，开始遍历边长k+1
            return bfs(x, y, k + 1)

        res = 0
        for x in range(row):
            for y in range(col):
                if matrix[x][y] == "1":
                    tem = bfs(x, y, 1)+1
                    # print(tem)
                    res = max(res, tem)
        return res**2
        

# @lc code=end