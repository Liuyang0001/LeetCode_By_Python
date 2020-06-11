#
# @lc app=leetcode.cn id=1530 lang=python3
#
# [1530] check-if-a-string-can-break-another-string
#
from itertools import permutations
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        def helper(a,b):
            n = len(a)
            for i in range(n):
                if a[i]>b[i]:
                    return False
            return True
    
        # for i in permutations(s1):
        #     for j in permutations(s2):
        #         print(i,j)
        #         if helper(i,j) or helper(j,i):
        #             return True
        # return False
        a = sorted(s1)
        b = sorted(s2)
        return helper(a,b) or helper(b,a)
                
# @lc code=end