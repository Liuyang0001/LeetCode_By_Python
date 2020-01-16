'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone_dict-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


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
