#
# @lc app=leetcode.cn id=1515 lang=python3
#
# [1515] find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
#
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] <= k:
            fib.append(fib[-1] + fib[-2])
        ans = 0
        while k > 0 and fib[-1] > 1:
            if k >= fib[-1]:
                ans += 1
                k -= fib[-1]
            else:
                fib.pop()
        return ans + k
# @lc code=end