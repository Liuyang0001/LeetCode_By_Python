#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] recover-binary-search-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tree = []
        def helper(root,flag):
            if not root:
                return
            helper(root.left,flag)
            if flag=="traverse":
                tree.append(root.val)
            elif flag == "modify":
                # print("更改前：",root.val)
                root.val = tree[0]
                del tree[0]
                # print("更改后：",root.val)
            helper(root.right, flag)
        
        helper(root, flag="traverse")
        # print(tree)
        tree.sort()
        # print(tree)
        helper(root, flag="modify")

# @lc code=end