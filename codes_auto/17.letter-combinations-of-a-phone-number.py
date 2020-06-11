#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] letter-combinations-of-a-phone-number
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 电话号与九宫格字母相对应
        phone_dict = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']}
        # 空字符串
        if not digits:
            return []
        res = []

        # 回溯函数
        def dfs(digits_cut, tmp):
            # 遍历到最后一个字母，返回上一层
            if(digits_cut == ""):
                res.append(tmp)
                return
            for c in phone_dict[digits_cut[0]]:
                # 递归下一位字母
                dfs(digits_cut=digits_cut[1:], tmp=tmp + c)
        # 调用回溯函数
        dfs(digits, "")
        return res
# @lc code=end