#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 阶乘表
        fac = [1,1,2,6,24,120,720,5040,40320,362880]
        nums = [i for i in range(1, n + 1)]
        # 回溯函数
        def backTrack(nums,tmp, k):
            if not nums:
                return tmp
            for i in range(len(nums)):
                if fac[len(nums)-1] < k:
                    k -= fac[len(nums)-1]
                    continue
                return backTrack(nums[:i]+nums[i+1:], tmp+str(nums[i]), k)
        return backTrack(nums,"", k)

# @lc code=end

