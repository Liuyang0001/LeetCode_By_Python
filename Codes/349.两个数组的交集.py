#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
from typing import List
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        nums1,nums2 = set(nums1),set(nums2)
        # n1, n2 = len(nums1), len(nums2)
        # if n1 > n2: nums1, nums2 = nums2, nums1
        res = []
        for i in nums1:
            if i in nums2: res.append(i)
        return res
# @lc code=end