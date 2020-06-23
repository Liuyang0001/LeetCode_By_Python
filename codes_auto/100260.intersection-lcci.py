#
# @lc app=leetcode.cn id=100260 lang=python3
#
# [100260] intersection-lcci
#
class Solution:
    def intersection(self, start1: List[int], end1: List[int],\
                     start2: List[int], end2: List[int]) -> List[float]:
        
        def getLine(start, end):
            x1, y1 = start
            x2, y2 = end
            return (y2 - y1, x1 - x2, x2 * y1 - x1 * y2)

        def inLine(x, y):
            for s, e in ((start1, end1), (start2, end2)):
                mnx = min(s[0], e[0])
                mxx = max(s[0], e[0])
                mny = min(s[1], e[1])
                mxy = max(s[1], e[1])
                if not (mnx <= x <= mxx and mny <= y <= mxy):
                    return False
            return True

        a1, b1, c1 = getLine(start1, end1)
        a2, b2, c2 = getLine(start2, end2)
        if a1 * b2 == a2 * b1:
            # 平行
            if c1 != c2:
                return []
            # 共线, 需要额外判断交点是否在两条线段上
            res = []
            for p in (start1, end1, start2, end2):
                if inLine(p[0], p[1]):
                    if not res or p[0] < res[0] or p[0] == res[
                            0] and p[1] < res[1]:
                        res = p
            return res

        # 不平行, 分母不为0
        # 可以计算交点了
        x = (c2 * b1 - c1 * b2) / (a1 * b2 - a2 * b1)
        y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
        if inLine(x, y):
            return [x, y]
        else:
            return []
# @lc code=end