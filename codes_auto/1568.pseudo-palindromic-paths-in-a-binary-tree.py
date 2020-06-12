#
# @lc app=leetcode.cn id=1568 lang=python3
#
# [1568] pseudo-palindromic-paths-in-a-binary-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        
        def helper(root,tem):
            if not root: return
            helper(root.left,tem+[root.val])
            helper(root.right,tem+[root.val])
            tem.append(root.val)
            if not root.left and not root.right:
                cnt = 0
                for i in Counter(tem).values():
                    if i%2: cnt+=1
                if cnt<2: self.ans+=1
    
        helper(root,[])
        return self.ans
        
# @lc code=end