#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
from typing import List
# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [0] * n
        # 每个数字的角标计数
        primes_cnt = [0] * len(primes)
        uglies[0] = 1
        for i in range(1, n):
            uglies[i] = min(x * uglies[y] for x, y in zip(primes, primes_cnt))
            for j in range(len(primes)):
                if uglies[i] >= primes[j] * uglies[primes_cnt[j]]:
                    primes_cnt[j] += 1
        return uglies[-1]
# @lc code=end

