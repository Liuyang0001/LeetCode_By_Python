#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] verify-preorder-serialization-of-a-binary-tree
#
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        n0, n12 = 0, 0
        for i in preorder.split(","):
            if n0 > n12: return False
            if i == "#": n0 += 1
            else: n12 += 1
        return n0 - n12 == 1
            
# @lc code=end