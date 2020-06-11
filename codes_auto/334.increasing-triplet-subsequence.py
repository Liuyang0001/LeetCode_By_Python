#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] increasing-triplet-subsequence
#
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i]==3: return True
        return False

# @lc code=end