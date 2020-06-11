#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] search-insert-position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return len([i for i in nums if i<target])
        nums_len = len(nums)
        if nums_len==0: return 0
        left,right = 0,nums_len-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target and nums[mid-1]<target:
                return mid
            if nums[mid]>=target:
                right = mid-1
            else:
                left = mid+1
        return left
# @lc code=end