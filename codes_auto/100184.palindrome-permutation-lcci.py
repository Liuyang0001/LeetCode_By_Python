#
# @lc app=leetcode.cn id=100184 lang=python3
#
# [100184] palindrome-permutation-lcci
#
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hash_list = {}
        count = 0
        for i in s:
            if hash_list.get(i,0)==0:
                hash_list[i]=1
                count+=1
            elif hash_list[i]%2==1:
                hash_list[i]+=1
                count-=1
            else:
                hash_list[i]+=1
                count+=1
        # print(hash_list)
        # print("count",count)
        return count<=1

                
# @lc code=end