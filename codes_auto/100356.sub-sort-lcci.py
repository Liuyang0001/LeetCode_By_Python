#
# @lc app=leetcode.cn id=100356 lang=python3
#
# [100356] sub-sort-lcci
#
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        n = len(array)
        if n < 2: return [-1, -1]
        # 从左到右，找到最后一个比其左边的最大值要小的元素array[y]
        y, maxv = -1, array[0]
        for i in range(1, n):
            if array[i] < maxv:
                y = i
            else: 
                maxv = array[i]
        # 如果没有的话说明整个序列是有序的，返回[-1,-1]
        if y == -1: return [-1, -1]
        # 从右到左，找到最后一个比其右边的最小值要小的元素array[x]，返回[x, y]
        x, minv = n, array[-1]
        for j in range(n-2, -1, -1):
            if array[j] > minv: 
                x = j
            else: 
                minv = array[j]
        return [x, y]

# @lc code=end