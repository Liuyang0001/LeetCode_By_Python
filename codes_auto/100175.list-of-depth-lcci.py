#
# @lc app=leetcode.cn id=100175 lang=python3
#
# [100175] list-of-depth-lcci
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree: return None
        que = [tree]
        res = []
        last_node = None
        while que:
            for _ in range(len(que)):
                cur_node = que.pop()
                # print(cur_node.val)
                if cur_node.left: 
                    que.insert(0,cur_node.left)
                if cur_node.right:
                    que.insert(0,cur_node.right)
                tem = ListNode(cur_node.val)
                if last_node:
                    last_node.next =tem
                else:
                    res.append(tem)
                last_node = tem
            last_node = None
        return res
                

# @lc code=end