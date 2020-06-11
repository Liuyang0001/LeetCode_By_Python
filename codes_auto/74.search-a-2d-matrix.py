#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] search-a-2d-matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = str(matrix)
        if re.findall("[^0-9\-]"+str(target)+"[^0-9]", s):
            return True
        else:
            return False
# @lc code=end