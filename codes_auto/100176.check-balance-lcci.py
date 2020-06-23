#
# @lc app=leetcode.cn id=100176 lang=python3
#
# [100176] check-balance-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def deep_of_tree(root):
            if not root: return 0
            left = deep_of_tree(root.left)
            right = deep_of_tree(root.right)
            if abs(left-right)>1:
                self.res = False
            return max(left,right)+1
        deep_of_tree(root)
        return self.res
# @lc code=end