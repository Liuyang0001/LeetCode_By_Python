#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        que = [root]
        while que:
            cur = que.pop(0)
            if cur.left:
                que.append(cur.left)
                if cur.left.left==cur.left.right== None:
                    res += cur.left.val
            if cur.right: que.append(cur.right)
        return res
# @lc code=end

