'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"

示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

'''

# 方法一：暴力法
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         res = ""
#         if len(strs)==0:
#             return res
#         #i的范围：[0,最短的字符串长度]
#         #j的范围：[0,字符串的数量-1]
#         for i in range(len(min(strs, key=len))):
#             for j in range(len(strs)-1):
#                 if strs[j][i] != strs[j+1][i]:
#                     return res
#             res += strs[0][i]
#         return res


# 方法二：利用zip绑定成列表，set去重
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:     
        res = ""
        # 使用*解包将每一位的字符分别打包成一个列表
        for i in zip(*strs):
            # 去重后列表只剩一个元素
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res