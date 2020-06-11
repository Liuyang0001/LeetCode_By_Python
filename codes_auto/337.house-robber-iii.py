#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] house-robber-iii
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        def dfs(root) -> [int, int]:
            if not root: return [0, 0]
            if not root.left and not root.right:
                return [root.val, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            return [ root.val + left[1] + right[1], \
                max(left[0] + right[0], left[0] + right[1],\
                    left[1] + right[0], left[1] + right[1])]
        return max(dfs(root))
# @lc code=end