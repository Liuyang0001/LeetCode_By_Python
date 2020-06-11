#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 3sum-closest
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3:
            return sum(nums)
        nums.sort()
        d_value = sys.maxsize
        for i in range(len(nums)):
            low,high = i+1,len(nums)-1
            while(low < high):
                x = target-nums[low]-nums[high]-nums[i]
                if abs(x) < abs(d_value):
                    d_value = x
                if x>0:
                    low+=1
                elif x<0:
                    high-=1
                else:
                    return target
        return target-d_value
# @lc code=end