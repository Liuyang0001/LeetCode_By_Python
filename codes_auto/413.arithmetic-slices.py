#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] arithmetic-slices
#
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        dif = [0] * (len(A) - 1)
        dif[0] = A[1] - A[0]
        dp = [0]*len(A)
        for i in range(2, len(A)):
            dif[i-1] = A[i] - A[i-1]
            if dif[i-1] == dif[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
# @lc code=end