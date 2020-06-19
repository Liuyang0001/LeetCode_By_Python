#
# @lc app=leetcode.cn id=1093 lang=python3
#
# [1093] recover-a-tree-from-preorder-traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dic = {-1: TreeNode(0)}     #字典初始化

        def addNode(v, p):          #添加树函数
            dic[p] = TreeNode(int(v))
            if not dic[p - 1].left: #左子树不存在就加在左边
                dic[p - 1].left = dic[p]
            else:                   #反之加在右边
                dic[p - 1].right = dic[p]
        
        val, dep = '', 0            #值和对应深度初始化
        for c in S:
            if c != '-':
                val += c            #累加字符来获得数字
            elif val:               #如果是‘-’且存在val
                addNode(val, dep)   #就把累加好的数字和对应深度添加进树
                val, dep = '', 1    #值和对应深度重新初始化
            else:
                dep += 1            #连续的‘-’只加深度不加值
        addNode(val, dep)           #末尾剩余的数字也要加进树
        return dic[0]

# @lc code=end