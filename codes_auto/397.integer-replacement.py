#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] integer-replacement
#
class Solution:
    def integerReplacement(self, n: int) -> int:
        def helper(n):
            if n == 1: return 0
            if n % 2 == 0:
                return helper(n//2)+1
            else:
                cnt1 = helper(n+1)+1
                cnt2 = helper(n-1)+1
                return min(cnt1, cnt2)
            
        return helper(n)
# @lc code=end