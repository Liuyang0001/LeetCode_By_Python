#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # path = path.replace("//","/")
        p = path.split("/")
        stack = []
        for i in p:
            if i not in ["", ".", ".."]:
                stack.append(i)
            elif i == ".." and stack:
                stack.pop()
        return "/"+"/".join(stack)
                
# @lc code=end