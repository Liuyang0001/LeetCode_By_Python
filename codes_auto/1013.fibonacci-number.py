#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] fibonacci-number
#
class Solution:
    @functools.lru_cache(None)
    def fib(self, N: int) -> int:
        memo = [0,1]
        for _ in range(N-1):
            memo.append(memo[-1]+memo[-2])
        return memo[N]
        # if N in [1,2]: return 1
        # return self.fib(N-1)+self.fib(N-2)
# @lc code=end