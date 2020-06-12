#
# @lc app=leetcode.cn id=1575 lang=python3
#
# [1575] maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
#
class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        x,y = [],[]
        hc.sort()
        vc.sort()
        last = 0
        x_max,y_max = 0,0
        for i in hc+[h]:
            x_max = max(x_max,i-last)
            last = i
        last = 0
        for j in vc+[w]:
            y_max = max(y_max,j-last)
            last =j
        print(x_max,y_max)
        return (x_max*y_max)%(10**9+7)
# @lc code=end