#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] majority-element
#
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        for num in c:
            if c[num] > (n // 2):
                return num
# @lc code=end