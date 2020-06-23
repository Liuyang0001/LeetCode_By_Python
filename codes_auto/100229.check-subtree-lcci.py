#
# @lc app=leetcode.cn id=100229 lang=python3
#
# [100229] check-subtree-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        
        # 检查两颗树是否相同
        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
            # 两个空结点
            if not p and not q:
                return True
            # 结点均非空且值相等
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)     
            return False
        
        # 层序遍历
        que = [t1]
        while que:
            cur_node = que.pop()
            if cur_node.val==t2.val and isSameTree(cur_node,t2):
                return True
            if cur_node.left:
                que.insert(0,cur_node.left)
            if cur_node.right:
                que.insert(0,cur_node.right)
        return False
# @lc code=end