#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] binary-tree-preorder-traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        def helper(root):
            if not root: return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res
# @lc code=end