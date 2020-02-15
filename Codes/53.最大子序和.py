#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
                print(nums)
            max_sum = max(nums[i], max_sum)

        return max_sum

# @lc code=end


if __name__ == "__main__":
    S = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(nums)
    print(S.maxSubArray(nums))
