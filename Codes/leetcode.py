from typing import List
from collections import defaultdict

# 链表的结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 树的结点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前缀树的结点
class TrieNode():
    def __init__(self):
        self.chrild = defaultdict(TrieNode)
        self.is_word = False