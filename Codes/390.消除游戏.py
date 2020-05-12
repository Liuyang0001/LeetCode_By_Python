#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] 消除游戏
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n < 2: return n
        return 2*(n//2+1-self.lastRemaining(n//2))
# @lc code=end

# 假如输入为n,我们使用f(n)表示从左到右(forward)的结果，
# 使用b(n)表示 从右到左(backward)的最终结果。
# 
# 则：
# 当 n = 1 时，存在 f(n) = 1, b(n) = 1
# 对于任意 n，存在 f(n) + b(n) = n + 1
# 对于 n > 2 的情况下，f(n) = 2 * b(n / 2)
# 所以：f(n) = 2 * (n / 2 + 1 - f(n / 2))