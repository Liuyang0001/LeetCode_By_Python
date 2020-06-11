#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] validate-binary-search-tree
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
        s = [float("-inf")]
        self.res = True
        def preorder(root):
            if not root: return 
            preorder(root.left)
            if root.val>s[-1]: 
                s.append(root.val)
            else: 
                self.res=False
                return
            preorder(root.right)

        preorder(root)
        return self.res
# @lc code=end