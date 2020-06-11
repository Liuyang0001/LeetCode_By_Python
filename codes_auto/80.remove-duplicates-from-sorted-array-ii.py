#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] remove-duplicates-from-sorted-array-ii
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #双指针+计数器
        count=1#元素出现的次数
        n=len(nums)
        L,R=1,1
        while R<n:
            if nums[R]==nums[R-1]:#出现重复元素，记录出现的次数
                count+=1
            else:count=1#若不是重复元素，重置计数器
            if count<=2:#若只有2个及以下的重复元素，移动L
                nums[L]=nums[R]
                L+=1
            R+=1
        return L

# @lc code=end