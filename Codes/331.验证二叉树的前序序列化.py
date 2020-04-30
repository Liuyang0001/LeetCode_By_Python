#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        n0, n12 = 0, 0
        for i in preorder.split(","):
            if n0 > n12: return False
            if i == "#": n0 += 1
            else: n12 += 1
        return n0 - n12 == 1
            
# @lc code=end
# 把空节点当作叶子结点来看
# 叶子节点数总是比非叶子节点数多一。根据前序遍历过程，
# 先遍历的非叶子节点数总是比叶子节点数多。