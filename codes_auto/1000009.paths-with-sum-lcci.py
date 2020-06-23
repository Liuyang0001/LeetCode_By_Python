#
# @lc app=leetcode.cn id=1000009 lang=python3
#
# [1000009] paths-with-sum-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0 # 特判
        self.coount = 0 # 路径的计数
        res = [] # 存储所有的路径
        def dfs(root,target,path):
            if target==sum:
                self.coount+=1
                # res.append(path)
            if root.left:
                dfs(root.left,target+root.left.val,path+[root.left.val])
            if root.right:
                dfs(root.right,target+root.right.val,path+[root.right.val])
        
        # 层序遍历 
        # 以当前结点为根结点的路径
        que = [root]
        while que:
            cur_node = que.pop()
            dfs(cur_node,cur_node.val,[cur_node.val])
            if cur_node.left:
                que.insert(0,cur_node.left)
            if cur_node.right:
                que.insert(0,cur_node.right)

        # print(res)
        return self.coount
# @lc code=end