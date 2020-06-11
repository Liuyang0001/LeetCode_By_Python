#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] guess-number-higher-or-lower-ii
#
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 分治函数
        @functools.lru_cache(None)
        def solve(l, r):
            if l == r: return 0
            if r - l == 1: return l
            if r - l == 2: return l + 1
            # res = sum(range(r))
            res = float("inf") # 初始为最大值
            for x in range((l+r)//2, r):
                res = min(max(solve(l, x-1), solve(x+1, r))+x, res)
            return res
        
        return solve(1, n)

# @lc code=end