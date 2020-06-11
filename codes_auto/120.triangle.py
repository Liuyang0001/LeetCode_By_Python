#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] triangle
#
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
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