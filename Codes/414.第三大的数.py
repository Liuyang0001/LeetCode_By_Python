#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
from typing import List
# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one, two, three = float("-inf"), float("-inf"), float("-inf")
        for i in nums:
            if i in [one,two,three]: continue
            if i > one:
                one, two, three = i, one, two
            elif i > two:
                one, two, three = one, i, two
            elif i > three:
                three = i
            print(one, two, three)
        return three if three!=float("-inf") else one
        
# @lc code=end

