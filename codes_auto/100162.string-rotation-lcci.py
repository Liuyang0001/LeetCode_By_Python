#
# @lc app=leetcode.cn id=100162 lang=python3
#
# [100162] string-rotation-lcci
#
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if n1!=n2: return False
        if s1==s2: return True
        point = s1[0]
        for i in range(n1):
            if s2[i]==point and s1==s2[i:]+s2[:i]:
                return True
        return False

# @lc code=end