#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        que = [root]
        res = []
        while que:
            n = len(que)
            for i in range(n):
                cur = que.pop(0)
                if i == n - 1: res.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
        return res

# @lc code=end