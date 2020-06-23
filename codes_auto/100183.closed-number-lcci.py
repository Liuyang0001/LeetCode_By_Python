#
# @lc app=leetcode.cn id=100183 lang=python3
#
# [100183] closed-number-lcci
#
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        num_bin = bin(num)[2:]
        cut_by_10 = num_bin.split("10")
        cut_by_01 = num_bin.split("01")
        n10,n01 = len(cut_by_10),len(cut_by_01)
        small_one,big_one = "-0b1","-0b1"
        if n01==n10==1:
            return [int(num_bin+"0",2),-1]
        if n10==1:
            small_one = "-0b1"
        else:
            tem = cut_by_10[-1].count("1")*"1"+cut_by_10[-1].count("0")*"0"
            small_one = "10".join(cut_by_10[:-1])+"01"+ tem
        if n01==1:
            big_one = num_bin+"0"
        else:
            tem = cut_by_01[-1].count("0")*"0"+cut_by_01[-1].count("1")*"1"
            big_one = "01".join(cut_by_01[:-1])+"10"+tem
        # print("num bin:", num_bin)
        # print("cut by 01:",cut_by_01)        
        # print("big:",big_one)
        # print("cut by 10:",cut_by_10)
        # print("sma:",small_one)
        # print(int(big_one,2),int(small_one,2))
        return [int(big_one,2),int(small_one,2)]
# @lc code=end