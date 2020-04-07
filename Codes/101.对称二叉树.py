#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 判断当前两个结点是否不同
        def dfs(left, right):
            if (left == None and right == None):
                return True
            if (left == None or right == None):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)

# @lc code=end
