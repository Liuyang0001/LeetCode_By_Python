#
# @lc app=leetcode.cn id=1532 lang=python3
#
# [1532] reformat-the-string
#
class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        if n==1: return s
        num_dic = ["0","1","2","3","4","5","6","7","8","9"]
        nums = []
        strs = []
        res = ""
        for i in range(n):
            if s[i] in num_dic:
                nums.append(s[i])
            else:
                strs.append(s[i])
        # print(nums,strs)
        n1,n2 = len(nums),len(strs)
        if abs(n1-n2)>1:
            return ""
        elif n1>=n2:
            res = nums.pop(0)
        else:
            res = strs.pop(0)
        for _ in range(1, n):
            try:
                if res[-1] in num_dic:
                    res += strs.pop(0)
                else:
                    res += nums.pop(0)
            except:
                return ""
        return res
# @lc code=end