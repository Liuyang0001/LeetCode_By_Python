#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        c1, c2 = Counter(nums1), Counter(nums2)
        res = []
        for i in c1.keys():
            if i in c2:
                res += [i] * (min(c1[i], c2[i]))
        return res
# @lc code=end

