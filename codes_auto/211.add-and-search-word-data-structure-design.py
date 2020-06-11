#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] add-and-search-word-data-structure-design
#
# 前缀树结点
class TrieNode:
    def __init__(self):
        self.chrild = defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.res = False

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for letter in word:
            cur = cur.chrild[letter]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # cur = self.root
        self.res = False
        def dfs(root: TrieNode, s: str):
            if not root: return
            if not s:
                if root and root.is_word:
                    self.res = True
                return
            # 万能匹配
            if s[0] == ".":
                # 深度优先遍历chrild
                for node in root.chrild.values():
                    dfs(node, s[1:])
            else:
                root = root.chrild.get(s[0])
                # if not root: return
                dfs(root, s[1:])
        dfs(self.root, word)
        return self.res



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end