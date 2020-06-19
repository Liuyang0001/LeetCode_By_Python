#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] serialize-and-deserialize-binary-tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode)-> str:
        """
        Encodes a tree to a single string.
        """
        if not root: return "[]"
        # que = collections.deque()
        # que.append(root)
        que = [root]
        res = []
        while que:
            node = que.pop(0)
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else: res.append("null")
        print(res)
        return '[' + ','.join(res) + ']'


    def deserialize(self, data: str)-> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        if data=='[]': return None
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end