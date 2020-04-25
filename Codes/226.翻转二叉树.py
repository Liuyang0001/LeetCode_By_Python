#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
from leetcode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        que = [root]
        while que:
            cur = que.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left: que.append(cur.left)
            if cur.right: que.append(cur.right)
        return root
# @lc code=end