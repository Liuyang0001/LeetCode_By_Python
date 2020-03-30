#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp_list = [0] * (n + 1)
        dp_list[0] = 1
        dp_list[1] = 1
        # G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        for i in range(2, n + 1):
            for j in range(i):
                dp_list[i] += dp_list[j]*dp_list[i-j-1]
        
        return dp_list[-1]
# @lc code=end

