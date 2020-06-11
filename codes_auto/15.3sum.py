#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 3sum
#
class Solution:
    def threeSum(self, nums:List[int])->List[List[int]]:
        n = len(nums)
        if n<3: return []
        nums.sort() # 从小到大排序
        res = []
        # 从左侧开始逐渐选取一个值为定值
        for i in range(n-1):
            # 避免重复项，如 [-4, -1, -1, 0, 1, 2] 中由于两个 -1 导致的两个 [-1, 0, 1]
            if i > 0 and nums[i] == nums[i-1]: continue
            # 减少无关计算，定值大于 0 后，后面的都大于 0，没必要进行计算了
            if nums[i] > 0: break
            # 左指针随着定值的移动而移动
            l = i + 1
            r = n - 1
            # 获取右侧剩余的值中的与前面定值相加为 0 的两个值
            while l < r:
                # 先求和，减少因 if 判断导致的重复计算和增加内存空间
                tem = nums[i] + nums[l] + nums[r]
                # 满足条件，添加
                if  tem == 0:
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
                elif tem < 0: l += 1
                # 大于 0，右指针左移
                else: r -= 1

        return res
# @lc code=end