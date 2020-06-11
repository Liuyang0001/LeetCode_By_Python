#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] generate-parentheses
#
class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        ans = []
        def backtrack(tem, left, right):
            if len(tem) == 2 * N:
                ans.append(tem)
                return
            if left < N:
                backtrack(tem+'(', left+1, right)
            if right < left:
                backtrack(tem+')', left, right+1)

        backtrack(tem="",left=0,right=0)
        return ans
# @lc code=end