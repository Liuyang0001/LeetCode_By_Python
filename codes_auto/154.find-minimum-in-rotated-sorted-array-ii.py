#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] find-minimum-in-rotated-sorted-array-ii
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:  # mid == right
                right -= 1
        return nums[left]
                
            
        
# @lc code=end