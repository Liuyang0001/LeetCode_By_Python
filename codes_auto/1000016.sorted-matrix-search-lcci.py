#
# @lc app=leetcode.cn id=1000016 lang=python3
#
# [1000016] sorted-matrix-search-lcci
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.res = False
        # 二分查找的标准写法
        def bin_search(ls,left,right,target):
            while left<=right:
                mid = (left+right)//2
                tem = ls[mid] # 中点值
                if tem==target:  
                    self.res = True
                    break
                elif tem<target: left = mid+1
                elif tem>target: right = mid -1
        # 按行遍历
        for ls in matrix:
            if not self.res: # 剪枝，避免不必要的遍历
                bin_search(ls,0,len(ls)-1,target)
        return self.res
# @lc code=end