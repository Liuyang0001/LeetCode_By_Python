#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] container-with-most-water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,res = 0,len(height)-1,0
        while(left<right):
            if min(height[left],height[right])*(right-left) > res:
                res=min(height[left],height[right])*(right-left)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return res
# @lc code=end