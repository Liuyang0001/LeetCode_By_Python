# 给定一个字符串s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 1-中心扩展
class Solution:
    # 中心扩展
    def expandAroundCenter(self,s: str,left:int,right:int) -> str:
        L, R = left, right
        while L>= 0 and R< len(s) and s[L]==s[R]:
            L -= 1
            R += 1
        return s[L+1:R]
    # 求最长回文子串
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: # 长度小于等于1直接返回原字符串
            return s
        res = s[:1] # 初始化result为字符串首位
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            # 迭代res使其成为最长的子串
            res = max(len1,len2,res,key=len)
        return res

class Solution:
    # 马拉车算法
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        # 将一个可能是偶数长/奇数长的字符串，首位以及每个字符间添加#
        test = '#'+'#'.join(s)+'#'
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 0
        for i in range(len(test)):
            left = i - 1
            right = i + 1
            step = 0

            while left >= 0 and right < len(test) and test[left] == test[right]:
                left -= 1
                right += 1
                step += 1
            
            if step > max_len:
                max_len = step
                start = (i - max_len) // 2
        return s[start: start + max_len]