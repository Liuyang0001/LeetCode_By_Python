#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0  # 初始化当前能到达最远的位置
        # i为当前位置，jump是当前位置的跳数
        for i, jump in enumerate(nums):
            # 如果当前位置能到达，并且当前位置+跳数>最远位置
            if max_i >= i and i+jump > max_i:
                max_i = i+jump  # 更新最远能到达位置
        return max_i >= i


# @lc code=end
if __name__ == "__main__":
    nums = [6, 0, 0, 0, 0, 0]
    S = Solution()
    S.canJump(nums)
