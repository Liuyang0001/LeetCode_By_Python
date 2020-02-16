#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        res = []
        intervals.sort()
        for i in range(n-1):
            # 后一个区间中包含在前一个区间内的元素
            if intervals[i + 1][0] in range(intervals[i][0], intervals[i][1] + 1):
                # 新的区间范围
                l1, l2 = intervals[i][0], max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = [l1, l2]
                intervals[i] = "*"
        res = [ i for i in intervals if i != "*" ]
        return res
# @lc code=end
