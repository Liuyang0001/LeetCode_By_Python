#
# @lc app=leetcode.cn id=1529 lang=python3
#
# [1529] max-difference-you-can-get-from-changing-an-integer
#
class Solution:
    def maxDiff(self, num: int) -> int:
        if num<10: return 8
        a,b="",""
        s=str(num)
        n = len(s)
        if s[0]!="9":
            a = s.replace(s[0],"9")
        else:
            i=1
            while i<n-1 and s[i]=="9":
                i+=1
            if i==n-1 and s[i]=="9" : a=s
            else:
                a = s.replace(s[i],"9")
        # a = s.replace(s[0],"9")
        if s[0]!="1":
            b = s.replace(s[0],"1")
        else:
            i=1
            while i<n-1 and (s[i]=="1"or s[i]=="0"):
                i+=1
            if i==n-1 and (s[i]=="1"or s[i]=="0"): b=s
            else:
                b = s.replace(s[i],"0")
        # print(a,b)
        return int(a)-int(b)
            
# @lc code=end