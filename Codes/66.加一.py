#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import List
# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            num = "".join(str(item) for item in digits)
            num = int(num) + 1
            digits = [int(x) for x in str(num)]
        return digits
# @lc code=end
