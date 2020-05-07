#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#
import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomset = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.randomset:
            self.randomset.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomset:
            return False
        else:
            self.randomset.remove(val)
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.randomset)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

