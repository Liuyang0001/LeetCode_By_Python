#
# @lc app=leetcode.cn id=1516 lang=python3
#
# [1516] the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
#
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        maxnum = 3*(2**(n-1))
        if k>maxnum: return ""
        if k <= maxnum/3: 
            s = "a"
            res = k
        elif k<= 2*maxnum/3: 
            s= "b"
            k = k- maxnum/3
        else : 
            s = "c"
            k = k- 2*maxnum/3
        maxnum = maxnum//3
        for _ in range(n-1):
            tem = "abc".replace(s[-1],"")
            print(tem)
            if k<=maxnum//2:
                s+=tem[0]
            else:
                s+=tem[1]
                k-=maxnum//2
            maxnum = maxnum//2
            
        return s
            
        
        
# @lc code=end