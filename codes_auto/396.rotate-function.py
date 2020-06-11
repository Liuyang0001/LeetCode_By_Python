#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] rotate-function
#
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        sum_data =  sum(A)
        f0 = sum(i*num for i,num in enumerate(A))
        res = f0
        last = f0
        for i in range(1, n):
            cur = last - sum_data + n * A[i - 1]
            last = cur
            res = max(cur, res)
        return res
# @lc code=end