#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # last:剩下未排列的部分
        # tem: 当前生成的排列
        def backtrack(last, tmp):
            if not last:
                res.append(tmp)
                return 
            for i in range(len(last)):
                backtrack(last[:i] + last[i+1:], tmp + [last[i]])
        backtrack(nums, [])
        return res
# @lc code=end