#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] first-bad-version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=1,n
        while left<right:
            mid = (left+right)//2
            tem = isBadVersion(mid)
            if not tem:
                left = mid+1
            else:
                right=mid
        return right
# @lc code=end