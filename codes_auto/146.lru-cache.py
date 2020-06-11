#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] lru-cache
#
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 假如key在缓存中，需要先获取到key对应的值，然后删除这个
        # key，再重新插入一遍(插入时会自动放入到第一位)
        if(key in self.lru):
            value = self.lru[key]
            del self.lru[key]
            self.lru[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        # 如果key在缓存中，需要先将这个key删除，最后统一再插入
        if(key in self.lru):
            del self.lru[key]
        # 如果key不在缓存中，那么检查缓存是否满了
        # 如果满了就删掉最久没用过的那个元素
        else:
            if(len(self.lru)==self.capacity):
                self.lru.popitem(False)
        # 最后统一插入这个元素
        self.lru[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end