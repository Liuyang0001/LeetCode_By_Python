#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        # 链表转换成列表
        while head:
            nums.append(head.val)
            head = head.next
        # print(nums)
        def ListToBST(nums):
            if not nums:
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = ListToBST(nums[:mid])
            root.right = ListToBST(nums[mid+1:])
            return root

        return ListToBST(nums)
# @lc code=end

