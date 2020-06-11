#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] remove-duplicates-from-sorted-array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rear = 0
        n = len(nums)
        if n<2: return n
        for i in range(1,n):
            if nums[i]!=nums[rear]:
                nums[rear+1]=nums[i]
                rear+=1
        
        return rear+1
# @lc code=end