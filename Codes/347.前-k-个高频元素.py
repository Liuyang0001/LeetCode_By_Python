#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from collections import Counter
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        c = Counter(nums)
        lc = sorted(c.items(), key=lambda x: x[1], reverse=True)
        res = [lc[0][0]]
        for i in range(1, len(lc)):
            if k == 1: break
            k-=1
            res.append(lc[i][0])
            
        return res
# @lc code=end