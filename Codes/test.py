import bisect
from collections import OrderedDict
from itertools import permutations
from typing import List

citations = [5, 4, 4, 3, 1]
l1 = [1, 2]
l2 = [1]


class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        res = 0
        n = len(points)

        # 计算落在圆内的数量
        def helper(x, y, r):
            cnt=0
            for i in points:
                if (i[0]-x)**2+(i[1]-y)**2<=r**2:
                    cnt += 1
            return cnt

        # 三点确定一个圆
        def q_cycle(x1, y1, x2, y2, x3, y3):
            a = x1 - x2
            b = y1 - y2
            c = x1 - x3
            d = y1 - y3
            e = ((x1 * x1 - x2 * x2) + (y1 * y1 - y2 * y2)) / 2.0
            f = ((x1 * x1 - x3 * x3) + (y1 * y1 - y3 * y3)) / 2.0
            det = b * c - a * d
            if abs(det) < 1e-5:
                return (0, 0)
            x0 = -(d * e - b * f) / det
            y0 = -(a * f - c * e) / det
            # 计算半径
            radius = hypot(x1 - x0, y1 - y0)
            # 半径超了
            if radius>r: return (0,0)
            return (x0,y0)
       
        res = max(helper(0, 0, r),1)
        dic = set([(0,0)])
        for p1, p2, p3 in permutations(points, 3):
            x, y = q_cycle(p1[0], p1[1], points[p2][0],p2[1], p3[0], p3[1])
            if (x, y) not in dic:
                tem = helper(x,y,r)
                res = max(res, tem)
        return res