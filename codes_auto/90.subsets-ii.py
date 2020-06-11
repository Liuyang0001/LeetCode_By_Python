#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] subsets-ii
#
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(index, tem):
            res.append(tem)
            for i in range(index, n):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backtrack(i + 1, tem + [nums[i]])
        backtrack(0, [])
        return res
# @lc code=end