#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] sum-of-mutated-array-closest-to-target
#
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        pre=0
        for i, a in enumerate(arr):
            k=len(arr)-i        # k>0
            d=pre+a*k-target    #sum = pre + a*k .
            if d>=0:    #★下面这步操作非常666！
                return a-d//k-(2*(d%k)>=k)
            pre+=a
        return arr[-1]

# @lc code=end