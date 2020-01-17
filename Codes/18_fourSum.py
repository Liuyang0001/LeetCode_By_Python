'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:  # 不足四个数
            return []
        if len(nums) == 4:  # 正好四个数
            return [nums] if sum(nums) == target else []
        nums.sort()  # 排序
        # 最大的四个数和小于target，最小的四个数和大于target
        if sum(nums[:4]) > target or sum(nums[-4:]) < target:
            return []
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                low = j+1  # 双指针遍历
                high = len(nums)-1
                while low < high:
                    sum_four = nums[i]+nums[j]+nums[low]+nums[high]
                    cur_list = [nums[i], nums[j], nums[low], nums[high]]
                    if sum_four == target and cur_list not in res:
                        res.append(cur_list)
                    if sum_four <= target:
                        low += 1
                    elif sum_four > target:
                        high -= 1
        return res
