#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] symmetric-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper1(root):
            if not root: 
                yield None
                return
            yield root.val
            yield from helper1(root.left)
            yield from helper1(root.right)
        def helper2(root):
            if not root: 
                yield None
                return
            yield root.val
            yield from helper2(root.right)
            yield from helper2(root.left)
            
        # print(list(helper1(root)),list(helper2(root)))
        return list(helper1(root))==list(helper2(root))
        
        
# @lc code=end