#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x==0:
            return x
        left = 0
        right = x//2
        while left <= right:
            mid = left + (right - left) // 2
            tmp = mid * mid
            if tmp  ==  x:
                return mid
            elif tmp < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

if __name__ == "__main__":
    S = Solution()
    res = S.mySqrt(8)
    print(res)
        
# @lc code=end

