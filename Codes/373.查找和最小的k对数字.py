#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
import itertools
from typing import List
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return sorted(itertools.product(nums1,nums2),key=sum)[:k]
# @lc code=end

