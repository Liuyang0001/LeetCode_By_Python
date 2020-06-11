#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] binary-tree-level-order-traversal-ii
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(root, depth):
            if not root:
                return
            if depth == len(res):
                res.insert(0, [])
            res[-depth-1].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        
        helper(root, 0)
        return res
# @lc code=end