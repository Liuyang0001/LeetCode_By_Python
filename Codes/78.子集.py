#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 回溯函数
        def backtrack(index, tem):
            res.append(tem)
            for i in range(index,n):
                backtrack(i+1, tem+[nums[i]])
        
        backtrack(0, [])
        return res
# @lc code=end

