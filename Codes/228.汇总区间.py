#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start = end = nums[0]
        nums = nums + [float("inf")]
        res = []
        for i in nums:
            # print(start,end)
            if i == end+1: end += 1
            else:
                tem = "->"+str(end) if start!=end else ""
                if res: res[-1] += tem
                # 更新起始位置
                start=end=i
                res.append(str(start))
        # 去掉最后的“inf”
        return res[:-1]
# @lc code=end

