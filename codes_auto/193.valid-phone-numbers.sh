#
# @lc app=leetcode.cn id=193 lang=bash
#
# [193] valid-phone-numbers
#
# Read from the file file.txt and output all valid phone numbers to stdout.
# \d ＝ [0-9]
cat file.txt  | grep -P "^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$"
# @lc code=end