#
# @lc app=leetcode.cn id=195 lang=bash
#
# [195] tenth-line
#
# NR在awk中指行号
awk 'NR == 10' file.txt

# -n表示只输出匹配行，p表示Print
# sed -n 10p file.txt 

# tail -n +10表示从第10行开始输出
# tail -n+10 file.txt|head -1 
# @lc code=end