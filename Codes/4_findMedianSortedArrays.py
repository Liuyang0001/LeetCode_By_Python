# 题目说明
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。

# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0

# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是 (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        # 使得num2成为更长的表
        if n < m:
            return self.findMedianSortedArrays(nums2, nums1)
        start_pos = 0
        end_pos = 2 * m
        while start_pos <= end_pos:
            c1 = (start_pos + end_pos) // 2
            c2 = m + n - c1  # 因为数组从0开始，所以c1+c2=(m+n+1)-1
            # 切割nums1
            LMax1 = nums1[(c1 - 1) // 2] if c1 > 0 else (-1 * sys.maxsize)
            RMin1 = nums1[c1 // 2] if c1 < 2 * n else sys.maxsize
            # 切割nums2
            LMax2 = nums2[(c2 - 1) // 2] if c2 > 0 else (-1 * sys.maxsize)
            RMin2 = nums2[c2 // 2] if c2 < 2 * m else sys.maxsize
            # 不满足LMax<RMin 则进行调整切割位置
            if LMax1 > RMin2:
                end_pos = c1 - 1
            elif LMax2 > RMin1:
                start_pos = c1 + 1
            else: # 找到合适的c1
                break
        return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2.0

# 作者：dyce
# 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/ji-yu-bian-bian-xiong-de-shuo-ming-xue-xi-hou-shi-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。