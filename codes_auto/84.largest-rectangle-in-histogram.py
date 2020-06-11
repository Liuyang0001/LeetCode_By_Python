#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] largest-rectangle-in-histogram
#
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        # 在原柱子两端加上两个高度为0的柱子，便于计算边界
        heights = [0] + heights + [0]
        res = 0
        # 遍历：以第i根柱子为最高柱子所能延伸的最大面积
        # 即   找栈顶左右两边第一个比栈顶小的元素
        for i in range(len(heights)):
            # print(stack)
            # 调整位置
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            # 当前元素无论如何也要放进去，不同的只是需不需要pop来调整位置
            stack.append(i)
        return res



# @lc code=end