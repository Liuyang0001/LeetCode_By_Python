#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] remove-k-digits
#
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: return '0'
        stack = []
        
        for n in num:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        # 现在栈里是递增数列，k还没用完，当然是从大的开始删了
        for _ in range(k):
            stack.pop()
        
        ans = ''.join(stack).lstrip('0')
        # ans可能被strip空了
        return ans or '0'
# @lc code=end