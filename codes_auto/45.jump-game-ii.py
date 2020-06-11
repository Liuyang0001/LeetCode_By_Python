#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] jump-game-ii
#
class Solution:
    def jump(self, nums: List[int]) -> bool:
        step, l, r = 0, 0, 1
        while r < len(nums):
            # r为当前所能跳到的最远位置
            l, r = r, max(i + nums[i] for i in range(l, r)) + 1
            step += 1
        return step
# @lc code=end