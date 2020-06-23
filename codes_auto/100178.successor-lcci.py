#
# @lc app=leetcode.cn id=100178 lang=python3
#
# [100178] successor-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root: return None
        self.res = None
        self.flag = False
        def inorder(root):
            if not root: return
            inorder(root.left)
            print(root.val)
            if self.flag: 
                self.res = root
                self.flag = False
            if root.val==p.val: 
                self.flag = True
            inorder(root.right)
        
        inorder(root)
        return self.res
# @lc code=end