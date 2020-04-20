#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        for num in c:
            if c[num] > (n // 2):
                return num
# @lc code=end

