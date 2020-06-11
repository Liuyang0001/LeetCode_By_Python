#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] kth-largest-element-in-an-array
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        nums.sort(reverse= True)
        return nums[k-1]
# @lc code=end