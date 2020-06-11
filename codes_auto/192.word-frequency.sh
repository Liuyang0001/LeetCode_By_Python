#
# @lc app=leetcode.cn id=192 lang=bash
#
# [192] word-frequency
#
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n'|sort|uniq -c |sort -r|awk '{print $2" "$1}'

# cat ——浏览文件
# tr -s ——替换字符串（空格换为换行）保证了一行一个单词
# sort ——默认ASCII值排序，排序号后还会有重复
# uniq —— 去重，-c再输出重复次数。结果就是 ”4 abc“ abc出现了4次
# sort -r —— 反向排序，也就是从大到小。得到按频率高低的结果
# awk ——格式化输出，规定输出是先字符串再重复次数，所以先$2再$1，中间空格分隔
# @lc code=end