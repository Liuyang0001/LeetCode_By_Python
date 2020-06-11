#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] integer-to-roman
#
class Solution:
    def intToRoman(self, num: int) -> str:
        R_M=num//1000
        R_D=num%1000//500
        R_C=num%1000%500//100
        R_L=num%1000%500%100//50
        R_X=num%1000%500%100%50//10
        R_V=num%1000%500%100%50%10//5
        R_I=num%1000%500%100%50%10%5//1

        res=R_M*"M"
        if R_D==1 and R_C==4:
            res+="CM"
        elif R_D==0 and R_C==4:
            res+="CD"
        else:
            res+="D"*R_D+"C"*R_C
        if R_L==1 and R_X==4:
            res+="XC"
        elif R_L==0 and R_X==4:
            res+="XL"
        else:
            res+="L"*R_L+"X"*R_X
        if R_V==1 and R_I==4:
            res+="IX"
        elif R_V==0 and R_I==4:
            res+="IV"
        else:
            res+="V"*R_V+"I"*R_I
        return res
# @lc code=end