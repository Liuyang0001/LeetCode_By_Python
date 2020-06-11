#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] subtree-of-another-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        @functools.lru_cache(None)
        def isSame(s,t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val==t.val and isSame(s.left,t.left) \
                and isSame(s.right,t.right)

        if not t: return True
        if not s: return False
        return isSame(s,t) or \
            self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
# @lc code=end