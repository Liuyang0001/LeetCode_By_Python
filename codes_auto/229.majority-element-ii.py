#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] majority-element-ii
#
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        step = n // 3
        res = []
        last = float("inf")
        for i in range(n):
            if i + step >= n: break
            if nums[i]==last: continue
            if nums[i] == nums[i + step]:
                res.append(nums[i])
                last = nums[i]
        return res
# @lc code=end