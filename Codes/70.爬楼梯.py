#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 特判
        if n < 3:
            return n
        # 初始化dp数组
        dp_list = [0] * (n + 1)
        dp_list[1] = 1
        dp_list[2] = 2
        # 开始dp
        for i in range(3, n + 1):
            # dp公式：当前项=前两项之和
            dp_list[i] = dp_list[i - 1] + dp_list[i - 2]
        return dp_list[n]
# @lc code=end

