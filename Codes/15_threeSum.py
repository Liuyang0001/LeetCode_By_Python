'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        res = set()
        nums.sort()
        for i in range(len_nums-1):
            if nums[i] > 0:
                return list(res)
            low = i+1
            high = len_nums-1
            while low < high:
                sumOfThree = nums[i]+nums[low]+nums[high]
                if sumOfThree == 0:
                    res.add((nums[i], nums[low], nums[high]))
                if sumOfThree < 0:
                    low += 1
                elif sumOfThree >= 0:
                    high -= 1
        for l in res:
            l=list(l)
        return list(res)

# 解法二
class Solution:
    def threeSum(self, nums):
        # 从小到大排序
        nums.sort()
        res = []
        length = len(nums)
        # 从左侧开始逐渐选取一个值为定值
        for i in range(length):
            # 避免重复项，如 [-4, -1, -1, 0, 1, 2] 中由于两个 -1 导致的两个 [-1, 0, 1]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 减少无关计算，定值大于 0 后，后面的都大于 0，没必要进行计算了
            if nums[i] > 0:
                break
            # 左指针随着定值的移动而移动
            l = i + 1
            r = length - 1
            # 获取右侧剩余的值中的与前面定值相加为 0 的两个值
            while l < r:
                # 先求和，减少因 if 判断导致的重复计算和增加内存空间
                s = nums[i] + nums[l] + nums[r]
                # 满足条件，添加
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # 避免重复项
                    while (l < r) and (nums[l+1] == nums[l]):
                        l += 1
                    while (l < r) and (nums[r-1] == nums[r]):
                        r -= 1
                    # 满足后现指针均需移动，避免重复和无效计算
                    l += 1
                    r -= 1
                # 小于 0，左指针右移
                elif s < 0:
                    l += 1
                # 大于 0，右指针左移
                else:
                    r -= 1
        return res
