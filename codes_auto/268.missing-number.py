#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] missing-number
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0: return 0
        if n==1: return 1 if nums[0]==0 else 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return right if right != nums[right] else n
        
    
        
# @lc code=end