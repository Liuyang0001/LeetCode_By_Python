#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] populating-next-right-pointers-in-each-node
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

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        def levelorder(root,level,num):
            que = [root]
            last_node = None
            while que:
                p = que.pop()
                # print(p.val)
                num += 1
                # 上一个结点是否为上层最后结点
                if last_node:
                    last_node.next = p
                # 是否为当前层的最后结点
                if num == 2**level-1:
                    # print(num,level)
                    p.next = None
                    last_node = None
                    level += 1
                else:
                    last_node = p
                if p.left: que.insert(0,p.left)
                if p.right: que.insert(0,p.right)
        levelorder(root,1,0)
        return root
# @lc code=end