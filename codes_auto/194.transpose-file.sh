#
# @lc app=leetcode.cn id=194 lang=bash
#
# [194] transpose-file
#
# Read from the file file.txt and print its transposed content to stdout.
# 第一步：
# 获取列数
col_num=$(cat file.txt| head -n1 |awk '{print NF}')
# 第二步:
# 循环次数为列数,根据awk取列即可

for((li=1; li<=$col_num;li++));
do
  line=$(cat file.txt | awk '{print $'$li' }')
  echo $line
done
# @lc code=end