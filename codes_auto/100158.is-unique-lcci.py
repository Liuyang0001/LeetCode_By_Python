#
# @lc app=leetcode.cn id=100158 lang=python3
#
# [100158] is-unique-lcci
#
class Solution:
    def isUnique(self, astr: str) -> bool:
        hash_list = {}
        for i in astr:
            if hash_list.get(i,0):
                return False
            else:
                hash_list[i]=1
        return True
# @lc code=end