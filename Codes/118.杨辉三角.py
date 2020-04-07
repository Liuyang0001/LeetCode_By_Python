#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]
        while len(res) < numRows:
            tem = [a+b for a, b in zip(res[-1]+[0], [0]+res[-1])]
            # print(tem)
            res.append(tem)

        return res

# @lc code=end
# 杨辉三角：左右加0，再对位相加
# 1 ---第一个
# 0 1
# 1 0
# 1 1 ---第二个
# 0 1 1
# 1 1 0
# 1 2 1 ---第三个
# 0 1 2 1
# 1 2 1 0
# 1 3 3 1 ---第四个