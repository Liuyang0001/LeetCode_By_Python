#
# @lc app=leetcode.cn id=100230 lang=python3
#
# [100230] reverse-bits-lcci
#
class Solution:
    def reverseBits(self, num: int) -> int:
        # 对二进制以“0”做分割
        cut_list = bin(num)[2:].split('0')
        cut_num = len(cut_list)
        # 二进制全“1”的情况，最前面可加“1”
        if cut_num==1: return len(cut_list[0])+1
        res = 1
        # 遍历更新res
        for i in range(0,cut_num-1):
            tem = len(cut_list[i])+len(cut_list[i+1])+1
            if tem>res: res = tem 
        return res
# @lc code=end