#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import List
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp 直接在原有数组进行修改，到当前结点的最小值
        # 最终返回最后一行的最小值即可
        for row in range(len(triangle)):
            for col in range(len(triangle[row])):
                if row == 0:
                    continue
                if col == 0:
                    triangle[row][col] += triangle[row-1][0]
                elif col == len(triangle[row])-1:
                    triangle[row][col] += triangle[row-1][-1]
                else:
                    triangle[row][col] += min(triangle[row-1][col], \
                        triangle[row-1][col-1])
        print(triangle)
        return min(triangle[-1])            
# @lc code=end

