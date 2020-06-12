#
# @lc app=leetcode.cn id=1538 lang=python3
#
# [1538] maximum-points-you-can-obtain-from-cards
#
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = sum(cardPoints[-k:])
        nums = cardPoints[-k:]+cardPoints[:k]
        tem = res
        @functools.lru_cache(None)
        def helper(res,tem):
            for i in range(k):
                tem = tem-nums[i]+nums[i+k]
                res = max(res,tem)
            return res
        return helper(res,tem)
# @lc code=end