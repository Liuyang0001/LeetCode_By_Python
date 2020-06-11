#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] zigzag-conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2: # 该算法在小于2时，直接返回即可
            return s
        # 初始化一个长度为numRows的列表
        ls = ["" for _ in range(numRows)]
        flag, i = -1, 0
        for string in s:
            ls[i] += string
            if i % (numRows-1) == 0:
                flag = -flag
            i += flag
            
        return "".join(ls)



    
# @lc code=end