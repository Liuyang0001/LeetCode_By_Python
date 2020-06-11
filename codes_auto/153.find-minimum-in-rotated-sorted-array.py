#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] find-minimum-in-rotated-sorted-array
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # [mid,right]连续递增，在[left,mid]查找
            if nums[mid]<nums[right]:
                right = mid
            # [2 3 4 *5* 6 7 1]
            # [mid,right]不连续
            else:
                left = mid+1
        return nums[left]
# @lc code=end