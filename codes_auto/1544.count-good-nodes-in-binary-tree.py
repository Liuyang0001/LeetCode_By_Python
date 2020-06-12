#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] count-good-nodes-in-binary-tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        res = []
        dic = set()
        
        def helper(root,tem,dic):
            if not root: return
            helper(root.left,tem+[root],dic)
            helper(root.right,tem+[root],dic)
            tem.append(root)
            if not root.left and not root.right:
                # res.append(tem)
                # print(tem)
                tem_max = float("-inf")
                for i in tem:
                    # print(tem_max)
                    if i.val>=tem_max:
                        tem_max = i.val
                        if i not in dic:
                            dic.add(i)
                            self.ans+=1
                return
        helper(root,[],dic)
        # print(res) 
        return self.ans


        
# @lc code=end