#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] combinations
#
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return list(combinations(range(1,n+1),k))
        res = []
        def backtrack(i, k, tem):
            if k == 0:
                res.append(tem)
                return
            for j in range(i, n+1):
                backtrack(j + 1, k - 1, tem+[j])

        backtrack(1, k, [])
        return res    
# @lc code=end