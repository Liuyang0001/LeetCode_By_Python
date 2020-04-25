#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 只有一个1的为True
        return bin(n)[2:].count("1")==1 if n>=0 else False
# @lc code=end

