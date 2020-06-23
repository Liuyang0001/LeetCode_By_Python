#
# @lc app=leetcode.cn id=100241 lang=python3
#
# [100241] permutation-i-lcci
#
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        if n==0: return []
        if n==1: return [S]
        res = []
        def backtrack(tem,last):
            if len(tem)==n:
                res.append(tem)
                return
            for i in last:
                backtrack(tem+i,last.replace(i,""))
        backtrack("",S)
        return res
# @lc code=end