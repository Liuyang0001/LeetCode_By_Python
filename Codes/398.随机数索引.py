#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#
import random
# @lc code=start
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) < 1:
                # 以某一概率(1/count)抽样
                    res = i
                # 计数
                count += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

