#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: # 米有结点
            return False
        if not root.left and not root.right and root.val-sum == 0:
            return True
        return self.hasPathSum(root.left, sum - root.val) \
             or self.hasPathSum(root.right, sum - root.val)
        

# @lc code=end

