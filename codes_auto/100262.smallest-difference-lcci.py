#
# @lc app=leetcode.cn id=100262 lang=python3
#
# [100262] smallest-difference-lcci
#
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        m,n = len(a),len(b)
        i,j,res = 0,0,float("inf")

        while i<m and j<n:
            res = min(abs(a[i]-b[j]),res)
            if a[i]>b[j]: j+=1
            else: i+=1
        return res
# @lc code=end