#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] path-sum-ii
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(root: TreeNode, sum: int, tem: list):
            if not root:
                return
            if not root.left and not root.right and sum == root.val:
                res.append(tem + [root.val])
                return
            helper(root.left, sum - root.val, tem + [root.val])
            helper(root.right, sum - root.val, tem + [root.val])
        helper(root, sum, [])
        return res
# @lc code=end