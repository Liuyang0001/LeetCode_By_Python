#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] maximum-length-of-repeated-subarray
#
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        l1 = len(A) 
        l2 = len(B) 
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)] 
        for i in range(1,l1+1): 
            for j in range(1,l2+1): 
                if A[i-1] == B[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1 
        return max(max(row) for row in dp)

# dp数组：
#   3 2 1 4 7
# 1 0 0 1 0 0
# 2 0 1 0 0 0
# 3 1 0 0 0 0
# 2 0 2 0 0 0
# 1 0 0 3 0 0

# @lc code=end