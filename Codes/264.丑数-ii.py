#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 7: return n
        dp = [1 for _ in range(n)]
        # 三指针初始化
        i2, i3, i5 = 0, 0, 0
        for i in range(1,n):
            min_val = min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            dp[i] = min_val
            # 找出哪个指针对应的数造出了现在这个最小值，
            # 将指针前移一位
            if dp[i2]*2 == min_val:
                i2 += 1
            if dp[i3]*3 == min_val:
                i3 += 1
            if dp[i5]*5 == min_val:
                i5 += 1
            print(i2,i3,i5)
            print(dp)
        return dp[-1]

# @lc code=end           