#
# @lc app=leetcode.cn id=100177 lang=python3
#
# [100177] legal-binary-search-tree-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        nodes = []
        def inorder(root:TreeNode):
            if not root: return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
        inorder(root)
        print(nodes)
        return nodes==sorted(nodes) and len(nodes)==len(set(nodes))
# @lc code=end