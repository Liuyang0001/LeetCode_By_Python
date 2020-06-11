#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] minimum-size-subarray-sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        left, right = 0, 0
        res = float("inf")
        for right in range(1,n + 1):
            while sum(nums[left:right]) >= s:
                # print(nums[left:right])
                left += 1
                res = min(res,right-left+1)
        return res if res!=float("inf") else 0
# @lc code=end