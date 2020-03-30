#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
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
                # 注意:这里不能使用pop()
                # 排序不会改变pop的顺序
                root.val = tree[0]
                del tree[0]
            helper(root.right, flag)
        # 先遍历
        helper(root, flag="traverse")
        # 排序
        tree.sort()
        # 再替换
        helper(root, flag="modify")

# @lc code=end

