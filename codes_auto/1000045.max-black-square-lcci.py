#
# @lc app=leetcode.cn id=1000045 lang=python3
#
# [1000045] max-black-square-lcci
#
from collections import defaultdict
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        mxrow = defaultdict(int)
        mxcol = defaultdict(int)
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for r in range(rows)[::-1]:
            for c in range(cols)[::-1]:
                if matrix[r][c] == 0:
                    mxrow[r, c] = 1 + mxrow[r, c + 1]
                    mxcol[r, c] = 1 + mxcol[r + 1, c]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    mxsize = min(mxrow[r, c], mxcol[r, c])
                    cursize = 0 if not res else res[2]
                    for size in range(mxsize, cursize, -1):
                        if mxcol[r, c + size - 1] >= size and mxrow[r + size - 1, c] >= size:
                            res = [r, c, size]
                            break
        return res

# 动态规划
# 1.获取每个节点的最大黑边行和列
#     mxrow[r,c]为当前点往右的最大黑边行
#     mxcol[r,c]为当前点往下的最大黑边列
# 从右下角开始遍历得到它们, 这样能利用之前得到的结果
# 2.计算最大方阵
#     从左上角开始遍历, 针对黑节点, 找其黑边行和列的较小值, 作为size的最大值
#     然后递减size遍历, 如果找到一个符合条件的(右顶点和下顶点的边长度>=cursize)就break
#     注意一个优化操作是循环遍历到当前res size+1为止, 因为如果等于当前res size的话一定不满足要求了
# @lc code=end