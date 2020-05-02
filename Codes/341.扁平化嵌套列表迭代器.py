#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
from typing import List
# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
class NestedIterator(object):

    def __init__(self, nestedList) -> List[NestedInteger]:
        self.g = self.flatten(nestedList)
        self.tem = list(self.g)
        # print(self.tem)
    
    # 构造生成器
    def flatten(self,nestedList):
        for val in nestedList:
            if val.isInteger():
                yield val.getInteger()
            else:
                yield from self.flatten(val.getList())
    
    def next(self) -> int:
        if self.hasNext():
            return self.tem.pop(0)

    def hasNext(self)-> bool:
        return True if self.tem else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end