#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] same-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 两个空结点
        if not p and not q:
            return True
        # 结点均非空且值相等
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)     
        return False

# @lc code=end