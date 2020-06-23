#
# @lc app=leetcode.cn id=100200 lang=python3
#
# [100200] bracket-lcci
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(l,r,tem):
            if r>l:
                return
            if r==n:
                res.append(tem)
                return
            if l<n:
                dfs(l+1,r,tem+"(")
            if r<n:
                dfs(l,r+1,tem+")")
        dfs(0,0,"")
        return res
# @lc code=end