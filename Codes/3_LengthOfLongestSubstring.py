# 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。

# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0 # 如果字符串s为空，返回0
        lookup = [] # 初始化窗口
        max_len = 0 # 窗口长度
        cur_len = 0 # 当前子串长度
        # 遍历字符串s
        for i in range(len(s)):
            val = s[i]
            if not val in lookup: # 如果该值不在窗口中
                lookup.append(val) # 添加到窗口内
                cur_len += 1  # 当前长度+1
                
            else:# 如果该值在窗口中已存在
                index = lookup.index(val) # 获取其在窗口中的位置
                lookup = lookup[index+1:] # 移除该位置及之前的字符
                lookup.append(val) 
                cur_len = len(lookup) # 当前长度更新为窗口长度
            
            if cur_len > max_len: # 看是否需要更新最大长度值
                max_len = cur_len
        
        return max_len # 返回最大子串长度

