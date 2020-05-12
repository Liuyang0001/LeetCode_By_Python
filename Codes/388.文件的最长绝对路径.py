#
# @lc app=leetcode.cn id=388 lang=python3
#
# [388] 文件的最长绝对路径
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if "." not in input: return 0
        depth_dict = {0: 0}
        max_depth = 0
        for line in input.split("\n"):
            # print(line)
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            if "." in name:
                max_depth = max(max_depth, len(name) + depth_dict[depth])
            else:
                depth_dict[depth + 1] = len(name) + depth_dict[depth] + 1
            # print(depth_dict)
        return max_depth
# @lc code=end

