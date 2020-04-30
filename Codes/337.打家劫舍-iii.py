#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
from leetcode import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        # 返回的[a,b]分别代表偷与不偷当前结点的最大值
        def dfs(root) -> [int, int]:
            if not root: return [0, 0]
            if not root.left and not root.right:
                return [root.val, 0]
            left, right = dfs(root.left), dfs(root.right)
            # 偷当前结点，则不能偷他两个孩子结点
            # 不偷当前结点，则偷两个孩子结点有四种可能，取最大值
            return [ root.val + left[1] + right[1], \
                max(left[0] + right[0], left[0] + right[1],\
                    left[1] + right[0], left[1] + right[1]) ]
        return max(dfs(root))
# @lc code=end