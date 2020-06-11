#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] binary-tree-paths
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        def helper(root, tem):
            # print(root.val)
            if not root: return
            if not root.left and not root.right:
                tem += [str(root.val)]
                if len(tem)>1:
                    res.append("->".join(tem))
                else:
                    res.append(tem[0])
                return
            helper(root.left, tem + [str(root.val)])
            helper(root.right, tem + [str(root.val)])
            
        helper(root, [])
        return res
# @lc code=end