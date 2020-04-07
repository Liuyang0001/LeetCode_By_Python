#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        ls = []
        def proorder(root: TreeNode):
            if not root:
                return
            ls.append(root)
            proorder(root.left)
            proorder(root.right)
        proorder(root)
        for i in range(len(ls) - 1):
            ls[i].left = None
            ls[i].right = ls[i+1]
            
# @lc code=end

