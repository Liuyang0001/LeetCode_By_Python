#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#
import functools
# @lc code=start
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
                # 分别向左右寻找，取最大值
                res = min(max(solve(l, x-1), solve(x+1, r)) + x, res)
            return res
        
        return solve(1, n)

# @lc code=end
# 求最大值里的最小，即一直猜错，二分，直到最后一种可能。
# 当区间长度为 1 时（l == r），费用是 0。
# 当区间长度为 2 时（r - l == 1），费用是 l（较小的那个数）。
# 当区间长度为 3 时（r - l == 2），费用是 l + 1（中间那个数）。

# 区间长度更长，我们就直接分成两个区间做，取两个区间里最大的一个就成了。

# 但是这个切分点（代码里是 x）不好找，试了几种都不行，干脆枚举了，从 l + r // 2 开始一直到 r - 1。

# 这里必须使用 @functools.lru_cache(None) 装饰器，否则超时。