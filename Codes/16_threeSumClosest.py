'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 只有三个数字，直接相加返回
        if len(nums) == 3:
            return sum(nums)
        # 对nums进行排序
        nums.sort()
        # 初始差值为最大值
        d_value = sys.maxsize
        for i in range(len(nums)):
            # low=i+1为去除之前判断过得操作
            low, high = i+1, len(nums)-1
            while(low < high):
                x = target - nums[low] - nums[high] - nums[i]
                # 进行差值
                if abs(x) < abs(d_value):
                    d_value = x
                if x > 0:
                    low += 1
                elif x < 0:
                    high -= 1
                elif x = 0:
                    return target
        return target - d_value
