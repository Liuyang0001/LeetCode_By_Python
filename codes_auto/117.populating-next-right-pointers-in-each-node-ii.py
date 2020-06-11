#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] populating-next-right-pointers-in-each-node-ii
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        que = [root]
        last_node = None
        while que:
            for _ in range(len(que)):
                cur_node = que.pop()
                if last_node:
                    last_node.next = cur_node
                last_node = cur_node
                if cur_node.left: que.insert(0, cur_node.left)
                if cur_node.right: que.insert(0,cur_node.right)
            cur_node.next = None
            last_node = None
        return root
            
# @lc code=end