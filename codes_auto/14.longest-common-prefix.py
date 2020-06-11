#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] longest-common-prefix
#
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
# @lc code=end