#
# @lc app=leetcode.cn id=1553 lang=python3
#
# [1553] count-triplets-that-can-form-two-arrays-of-equal-xor
#
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n-1):
            a = arr[i]
            for j in range(i+1,n):
                a ^= arr[j]
                if a == 0:
                    res += j-i 
        return res
# @lc code=end