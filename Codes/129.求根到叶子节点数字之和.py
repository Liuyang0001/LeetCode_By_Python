#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
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
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root: TreeNode,tem: str):
            if not root:
                return
            if not root.left and not root.right:
                # print(tem+str(root.val))
                self.res += int(tem+str(root.val))
            dfs(root.left, tem + str(root.val))
            dfs(root.right, tem + str(root.val))

        dfs(root, "")
        return self.res
# @lc code=end

