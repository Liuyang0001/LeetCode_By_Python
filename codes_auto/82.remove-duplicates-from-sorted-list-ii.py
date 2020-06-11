#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] remove-duplicates-from-sorted-list-ii
#
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ls = []
        p = head
        while p:
            ls.append(p.val)
            p = p.next
        nums_dict = Counter(ls)
        H = ListNode(-1)
        p = H
        for i in nums_dict.keys():
            if nums_dict[i] == 1:
                p.next = ListNode(i)
                p = p.next
        return H.next

if __name__ == "__main__":
    S = Solution()
    ls = [1, 2, 3, 3, 4, 4, 5]
    H = ListNode(-1)
    p = H
    for i in ls:
        p.next = ListNode(i)
        p = p.next
    head = H.next
    res = S.deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next
# @lc code=end