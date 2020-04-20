#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
from typing import List
# @lc code=start
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==1: return str(nums[0])
        ls = [*map(str, nums)]
        # 自定义排序规则
        cmp = cmp_to_key(lambda b,a: int(a+b)-int(b+a))
        ls.sort(key=cmp)
        # print(ls)
        return "".join(ls).lstrip("0") or "0"
# @lc code=end

