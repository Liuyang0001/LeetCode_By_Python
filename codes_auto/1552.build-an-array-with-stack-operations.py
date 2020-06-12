#
# @lc app=leetcode.cn id=1552 lang=python3
#
# [1552] build-an-array-with-stack-operations
#
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        for i in range(1,n+1):
            if not target: break
            if i==target[0]:
                res.append("Push")
                del target[0]
            else:
                res.append("Push")
                res.append("Pop")
        return res
                
        
# @lc code=end