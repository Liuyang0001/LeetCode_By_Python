#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] h-index-ii
#
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        n = len(citations)
        # citations.sort()
        res = 0
        # 从后向前查找
        for c in citations[::-1]:
            # 二分查找索引，索引右侧则均>=c
            ind = bisect.bisect_left(citations, c)
            res = max(min(n-ind,c),res)
        return res
# @lc code=end