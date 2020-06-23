#
# @lc app=leetcode.cn id=100259 lang=python3
#
# [100259] words-frequency-lcci
#
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.book = collections.Counter(book)

    def get(self, word: str) -> int:
        return self.book.get(word,0)


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
# @lc code=end