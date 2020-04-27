#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3: return False
        result = []
        def dfs(begin, path, left_num):
            if len(path) > 2 and left_num == 0: # 数字被用完
                result.append(path)
                return
            for i in range(begin + 1, len(num) + 1):
                if i > begin + 1 and num[begin] == '0': return # 多位数字不能以0开头
                if len(path) < 2:
                    dfs(i, path + [int(num[begin:i])], len(num) - i)
                else:
                    if int(num[begin:i]) == path[-1] + path[-2]:
                        dfs(i, path + [int(num[begin: i])], len(num) - i)
        
        dfs(0, [], len(num))
        return  bool(result)
# @lc code=end

