#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] k-th-symbol-in-grammar
#
class Solution:
    def kthGrammar(self, N:int, K:int)->int:
        if N == 1: return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)//2)
# @lc code=end