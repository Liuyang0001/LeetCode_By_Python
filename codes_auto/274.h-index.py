#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] h-index
#
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        n = len(citations)
        citations.sort()
        # 从后向前查找
        res = 0
        for c in citations[::-1]:
            # 二分查找
            ind = bisect.bisect_left(citations, c)
            # print(ind)
            res = max(min(n-ind,c),res)
            # if n - ind >= c: return c
        return res
# @lc code=end