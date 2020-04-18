#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [*map(int,version1.split("."))]
        v2 = [*map(int,version2.split("."))]
        # [0]*负数=[]
        offset = (len(v2)-len(v1))
        v1, v2 = v1 + [0] * offset, v2 + [0] * (-offset)
        print(v1, v2)
        # True-False = 1
        return (v1>v2)-(v2>v1)
# @lc code=end

