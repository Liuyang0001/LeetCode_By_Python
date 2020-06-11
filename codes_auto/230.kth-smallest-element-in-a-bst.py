#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] kth-smallest-element-in-a-bst
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.count = 0
        def inorder(root,k):
            if not root: return
            inorder(root.left,k)
            self.count += 1
            # print(self.count,root.val)
            if self.count == k:
                self.res = root.val
                return
            inorder(root.right,k)
        
        inorder(root, k)
        return self.res
# @lc code=end