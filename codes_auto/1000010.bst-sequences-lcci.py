#
# @lc app=leetcode.cn id=1000010 lang=python3
#
# [1000010] bst-sequences-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []
        def findPath(cur, que, path):
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
            if not que:
                res.append(path)
                return
            for i, node in enumerate(que):
                newque = que[:i] + que[i+1:]
                findPath(node, newque, path + [node.val])


        findPath(root, [], [root.val])
        return res
# @lc code=end