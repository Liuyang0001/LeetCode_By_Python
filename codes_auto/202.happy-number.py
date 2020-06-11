#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] happy-number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n>1:
            n = sum([int(i)**2 for i in str(n)])
            if n not in memo:
                memo.add(n)
            else: return False
        return n==1
# @lc code=end