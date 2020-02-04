'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3

示例 2:

输入: [3,4,-1,1]
输出: 2

示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    # 3 应该放在索引为 2 的地方
    # 4 应该放在索引为 3 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            # i != nums[i]-1  这里外层套nums是防止[1,1]出现死循环
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1