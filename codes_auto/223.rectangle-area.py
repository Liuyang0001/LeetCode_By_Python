#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] rectangle-area
#
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 理解题意：每个矩形由其左下顶点和右上顶点坐标表示
        # 重合的总面积=投影到x轴重合的长度*投影到y轴重合的长度
        x,y = 0, 0
        if (min(C, G) > max(A, E) and min(D, H) > max(B, F)):
            x = abs(min(C, G) - max(A, E)) 
            y = abs(min(D, H) - max(B, F))
        return (C-A)*(D-B)+(G-E)*(H-F) - x*y
# @lc code=end