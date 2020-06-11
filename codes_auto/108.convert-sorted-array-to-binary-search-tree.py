#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] convert-sorted-array-to-binary-search-tree
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
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
# @lc code=end