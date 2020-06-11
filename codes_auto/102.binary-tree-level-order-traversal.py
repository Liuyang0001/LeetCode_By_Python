#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] binary-tree-level-order-traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        que  = [root]
        while que:
            res.append([])
            for _ in range(len(que)):
                cur = que.pop(0)
                res[-1].append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
        return res
# @lc code=end