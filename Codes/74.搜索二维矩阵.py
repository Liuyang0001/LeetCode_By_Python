#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
import re
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = str(matrix)
        # 利用正则去掉target前后均有数字的匹配项
        if re.findall("[^0-9\-]"+str(target)+"[^0-9]", s):
            return True
        else:
            return False
# @lc code=end

