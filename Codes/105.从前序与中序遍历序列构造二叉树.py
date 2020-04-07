#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        tem_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:tem_index+1],inorder[:tem_index])
        root.right = self.buildTree(preorder[tem_index+1:], inorder[tem_index+1:])
        
        return root
# @lc code=end

