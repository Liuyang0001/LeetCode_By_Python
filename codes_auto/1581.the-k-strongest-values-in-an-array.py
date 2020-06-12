#
# @lc app=leetcode.cn id=1581 lang=python3
#
# [1581] the-k-strongest-values-in-an-array
#
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        m = arr[(n-1)//2]
        # m = arr[(n-1)//2] if n%2 else (arr[n//2-1]+arr[n//2])/2
        # print(m)
        res = []
        for i in range(n):
            tem = abs(arr[i]-m)
            bisect.insort(res,(tem,arr[i]))
        # print(res)
        ans = []
        for i in range(1,k+1):
            # print(res[-i])
            ans.append(res[-i][1])
        return ans
        
        
# @lc code=end