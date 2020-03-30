#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
    def isValidBST(self, root: TreeNode) -> bool:
        tree = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            tree.append(root.val)
            helper(root.right)
        helper(root)
        # print(tree,sorted(tree))
        # 需判断是否存在重复结点
        return tree==sorted(tree) and len(set(tree))==len(tree)
# @lc code=end

