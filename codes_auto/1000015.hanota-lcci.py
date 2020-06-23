#
# @lc app=leetcode.cn id=1000015 lang=python3
#
# [1000015] hanota-lcci
#
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.move(n, A, B, C)
    # 定义move 函数移动汉诺塔
    def move(self,n, A, B, C):
        if n == 1:
            C.append(A[-1])
            A.pop()
            return 
        else:
            self.move(n-1, A, C, B)  # 将A上面n-1个通过C移到B
            C.append(A[-1])          # 将A最后一个移到C
            A.pop()                  # 这时，A空了
            self.move(n-1,B, A, C)   # 将B上面n-1个通过空的A移到C
# @lc code=end