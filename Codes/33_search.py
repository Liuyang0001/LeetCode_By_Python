'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid, left, right = 0, 0, len(nums)-1
        while left <= right:  # 二分法
            mid = (left + right) // 2

            # 找到该点索引值
            if nums[mid] == target:
                return mid

            # 旋转点T在mid右区间
            # [left......mid....T....right]
            if nums[left] <= nums[mid]:
                # target在[left,mid)的升序空间中
                if nums[left] <= target < nums[mid]:
                    right = mid
                # target在(mid,T]或者[T,right]中
                else:
                    left = mid + 1

            # 旋转点T在mid左区间
            # [left...T...mid........right]
            elif nums[left] > nums[mid]:
                # target在(mid,right]的升序空间中
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target在[left,T]或者[T，mid)
                else:
                    right = mid
        # 未找到该点
        return -1
