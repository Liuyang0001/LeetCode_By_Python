#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] pascals-triangle-ii
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res,num = [1],0
        while num < rowIndex:
            num += 1
            res = [a+b for a, b in zip([0]+res, res+[0])]
        return res
# @lc code=end