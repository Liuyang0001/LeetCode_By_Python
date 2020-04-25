#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            if dic[i] == 2:
                return True
        return False

# @lc code=end

