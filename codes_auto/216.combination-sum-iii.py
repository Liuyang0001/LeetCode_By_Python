#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] combination-sum-iii
#
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        res = []
        def helper(tem, nums, k, target):
            # print(tem, nums, k, target)
            if k == 0 and target == 0:
                res.append(tem)
                return
            if k < 0: return
            if not nums: return
            for i in range(len(nums)):
                # print(i)
                helper(tem + [nums[i]], nums[i+1:], k - 1, target - nums[i])
        helper([], nums, k, n)
        return res
# @lc code=end