#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
import functools
class Solution:
    # Notice：返回值应为List[TreeNode]
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        # 收集每次的返回值，组成缓存列表,None为动态调节大小
        @functools.lru_cache(None)
        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start, end + 1):
                # 左子树均小于val
                for left in helper(start, val - 1):
                    # 右子树均大于val
                    for right in helper(val + 1, end):
                        # 构建树节点
                        root = TreeNode(val,left,right)
                        res.append(root)
            # print(res)
            return res
        return helper(1, n)


# @lc code=end

