#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        res = ""  # 保存结果
        # 使用栈，这和简单括号匹配类似
        stack, cnt = [], 0  # 用来存储括号内容和重复个数
        for item in s:
            if item == "[":  # 将数字和括号里字母内容入栈
                stack.append([cnt, res])
                cnt, res = 0, ""  # 回复初始状态
            elif item == "]":  # 将数字和括号里的内容出栈
                cnt_out, res_out = stack.pop()
                # 嵌套情况：2[b2[c]]=> 这时的res=c,resout=b,cnt_out = 2 =>res="bcc"
                res = res_out + cnt_out*res
            elif "0" <= item <= "9":  # 转换数字
                cnt = cnt*10+int(item)
            else:  # item 为非括号的字母时，转换字符串
                res += item
        return res
# @lc code=end
