# 题目：
# 给出两个非空的链表用来表示两个非负的整数。
# 其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def ln2str(ln: ListNode):#链表转换为字符串
            if ln.next == None:
                return str(ln.val)
            else:
                return str(ln.val) + str(ln2str(ln.next))
                
        def str2ln(str_res: str):#字符串转换成链表
            if len(str_res)==1:
                return ListNode(int(str_res))
            else:
                ln_temp = ListNode(int(str_res[0]))
                ln_temp.next = str2ln(str_res[1:])
                return ln_temp

        str1 = ln2str(l1)[::-1] #将链表1转换为字符串并逆置
        str2 = ln2str(l2)[::-1] #将链表2转换为字符串并逆置
        str_res = str(int(str1)+int(str2))[::-1] #相加后转换为字符串，逆置
        return str2ln(str_res)  #返回转换成的链表

# 官方解法
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0) # 建立一个头结点
        curr, carry = dummyHead, 0 #curr表当前结点；carry表进位
        while l1 or l2: # 不全为空
            sum = 0
            if l1: # l1非空
                sum += l1.val
                l1 = l1.next
            if l2: # l2非空
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        if carry > 0: # 需要进位，使得链表加长
            curr.next = ListNode(1)
        return dummyHead.next; # 返回除头结点之后链表