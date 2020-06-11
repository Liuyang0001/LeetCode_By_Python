#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] remove-element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,0
        len_nums = len(nums)
        while j<len_nums:
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
            j+=1
        nums = nums[:i]
        return i
# @lc code=end