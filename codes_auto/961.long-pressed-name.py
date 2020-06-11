#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] long-pressed-name
#
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name: return True
        i,j = 0,0
        l1,l2 = len(name),len(typed)
        while i<l1 and j<l2:
            tem_i,tem_j = 0,0
            if name[i]!=typed[j]: return False
            tem = name[i]
            while i<l1 and name[i]==tem:
                tem_i+=1
                i+=1
            while j<l2 and typed[j]==tem:
                tem_j += 1
                j+=1
            if tem_i>tem_j: return False
        return i==l1 and j==l2

# @lc code=end