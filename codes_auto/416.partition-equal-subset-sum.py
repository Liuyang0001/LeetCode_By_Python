#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] partition-equal-subset-sum
#
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_of_num = sum(nums)
        if sum_of_num % 2 == 1: return False
        target = sum_of_num // 2
        nums.sort()
        # 剪枝
        if nums[-1] > target: return False
        if nums[-1] == target: return True
        dp = [0] * (target+1)
        for i in range(1, n):
            for v in range(target, nums[i]-1, -1):
                dp[v] = max(dp[v], dp[v-nums[i]]+nums[i])
        return dp[target] == target        
# @lc code=end