#
# @lc app=leetcode.cn id=100174 lang=python3
#
# [100174] minimum-height-tree-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        n = len(nums)
        if n==1: return TreeNode(nums[0])
        mid = n//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
# @lc code=end