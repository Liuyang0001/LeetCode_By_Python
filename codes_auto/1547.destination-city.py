#
# @lc app=leetcode.cn id=1547 lang=python3
#
# [1547] destination-city
#
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ls = list(zip(*paths))
        for i in ls[1]:
            if i not in ls[0]:
                return i
# @lc code=end