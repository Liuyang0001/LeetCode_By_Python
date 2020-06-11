#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] minimum-depth-of-binary-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution():
    def minDepth(self, root: TreeNode) -> int:  
        if not root: return 0
        left = self.minDepth(root.left) 
        right = self.minDepth(root.right) 
        if left == 0 or right == 0:
            return left + right + 1
        else:
            return min(left, right) + 1 


# @lc code=end