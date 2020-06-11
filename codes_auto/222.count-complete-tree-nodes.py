#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] count-complete-tree-nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res, que = 0, [root]
        while que:
            n = len(que)
            res += n
            for _ in range(n):
                cur = que.pop(0)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
        return res

# @lc code=end