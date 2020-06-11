#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] copy-list-with-random-pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def deepcopy(node, nodes_dic):
            if not node: return None
            if node in nodes_dic: return nodes_dic[node]
            cur = Node(node.val)
            nodes_dic[node] = cur
            cur.next = deepcopy(node.next, nodes_dic)
            cur.random = deepcopy(node.random, nodes_dic)
            return cur
        return deepcopy(head,{})
# @lc code=end