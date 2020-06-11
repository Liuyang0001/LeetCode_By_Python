#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] merge-sorted-array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=sorted(nums1[:m]+nums2)
# @lc code=end