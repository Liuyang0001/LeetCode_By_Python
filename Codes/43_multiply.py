'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1, num2 = num1[::-1], num2[::-1] # 反转方便遍历相乘
        lenNum = len(num1) + len(num2)  # 保存最终最大的数字
        returnNum = [0 for c in range(lenNum)]  # 用list先存储
        for index2 in range(len(num2)):
            multiplier2 = int(num2[index2])  # 就直接按照顺序放，最后再反过来！
            for index1 in range(len(num1)):
                multiplier1 = int(num1[index1])
                temp = multiplier2 * multiplier1 + returnNum[index1 + index2]
                if temp >= 10:  # 是否涉及进位问题
                    returnNum[index1 + index2] = temp % 10
                    returnNum[index1 + index2 + 1] += int(temp / 10)
                else:
                    returnNum[index1 + index2] = temp
        returnNum = returnNum[::-1]
        while returnNum and returnNum[0] == 0:
            del returnNum[0]  # 去除无效的0
        returnNum = [str(c) for c in returnNum]  # 将列表中的每一个元素转成字符串
        return ''.join(returnNum)
