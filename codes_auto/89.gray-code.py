#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] gray-code
#
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(2 ** n):
            # 最高位保留，其他位异或操作
            res.append(i ^ (i >> 1))
        return res
# @lc code=end