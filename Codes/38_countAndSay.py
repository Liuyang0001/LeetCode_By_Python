'''
外观数列 是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1. 1
2. 11
3. 21
4. 1211
5. 111221

1 被读作"一个一" , 即 11。
11 被读作"两个一", 即 21。
21 被读作"一个二" ,  "一个一" , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"

示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-and-say
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return '1'
        # 加上*，可以防止数组越界,不用考虑边界问题
        num = self.countAndSay(n-1)+"*"
        nums_ls = list(num)
        # print(nums_ls)
        count, res = 1, ""
        for i in range(len(nums_ls) - 1):
            # 计数重复的数值
            if nums_ls[i] == nums_ls[i+1]:
                count += 1
            elif nums_ls[i] != nums_ls[i+1]:
                res += str(count) + nums_ls[i]
                # print(res)
                count = 1
        return res

if __name__ == "__main__":
    S = Solution()
    # nums = [1, 5, 6, 6, 6, 7]
    # target = 7
    res = S.countAndSay(n=7)
    print(res)