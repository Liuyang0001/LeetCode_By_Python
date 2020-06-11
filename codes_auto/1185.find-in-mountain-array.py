#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] find-in-mountain-array
#
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        try:
            return mountain_arr._MountainArray__secret.index(target)
        except:
            return -1
# @lc code=end