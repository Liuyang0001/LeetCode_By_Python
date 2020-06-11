#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] pascals-triangle
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0: return []
        if numRows==1: return [[1]]
        def add(a,b):
            return [a[i]+b[i] for i in range(len(a))]
        res = [[1]]
        while numRows>1:
            res.append(add([0]+res[-1],res[-1]+[0]))
            numRows-=1
        return res
# @lc code=end