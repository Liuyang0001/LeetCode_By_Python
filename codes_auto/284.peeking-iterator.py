#
# @lc app=leetcode.cn id=284 lang=python3
#
# [284] peeking-iterator
#
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    """
    本题用另外两个变量self.flag来标记是否用了peek()；self.var来保存peek()所返回的值；
    如果在peek()后调用了next()；则将self.flag置0，并返回self.var；
    """
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.flag = 0
        self.var = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.flag == 0:
            self.flag = 1
            self.var = self.iterator.next()
        
        return self.var
        

    def next(self):
        """
        :rtype: int
        """
        if self.flag == 1:
            self.flag = 0
            return self.var
        else:
            return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.flag == 1:
            return True
        return self.iterator.hasNext()        


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end