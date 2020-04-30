#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
from typing import List
# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        # 求出单个数组可以组成i位的最大数组
        def getMaXArr(nums, i):
            if not i:
                return []
            # pop表示最多可以不要nums里几个数字，要不组成不了i位数字
            stack, pop = [], len(nums) - i
            for num in nums:
                while pop and stack and stack[-1] < num :
                    pop -= 1
                    stack.pop()
                stack.append(num)
            return stack[:i]
		
        def merge(tmp1, tmp2):
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        res = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                # 取num1的i位, num2的k - i
                tmp1 = getMaXArr(nums1, i)
                tmp2 = getMaXArr(nums2, k - i)
                # 合并
                tmp = merge(tmp1, tmp2)
                if res < tmp:
                    res = tmp
        return res
                
# @lc code=end
"""题意理解错误，以为是两个数组分别只能取最前面的数字
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def list2num(nums: List[int]) -> int:
            res = 0
            for i in nums:
                res = res * 10 + i
            return res
        def helper(nums1, nums2, tem, k):
            if k == 0: return tem
            # n1, n2 = len(nums1), len(nums2)
            if not nums1 and k > 0:
                return helper([], [], tem + nums2[:k], 0)
            if not nums1 and k > 0:
                return helper([], [], tem + nums1[:k], 0)
            if nums1[0] > nums2[0]:
                return helper(nums1[1:], nums2, tem + [nums1[0]], k - 1)
            elif nums1[0] < nums2[0]:
                return helper(nums1, nums2[1:], tem + [nums2[0]], k - 1)
            else:  # 两者相等
                tem1 = helper(nums1[1:], nums2, tem + [nums1[0]], k - 1)
                tem2 = helper(nums1, nums2[1:], tem + [nums2[0]], k - 1)
                c1, c2 = list2num(tem1), list2num(tem2)
                return tem1 if c1 > c2 else tem2
        return helper(nums1,nums2,[],k)
"""