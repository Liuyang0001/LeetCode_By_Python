#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] valid-parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        st = []
        for c in s:
            try:  # 异常处理
                if c in dic:
                    st.append(c)
                elif dic[st.pop()] != c:
                    return False
            # 空栈进行pop()会返回IndexError
            except IndexError:
                return False
        return len(st) == 0
# @lc code=end