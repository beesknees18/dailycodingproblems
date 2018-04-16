# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
# get(key): gets the value at key. If no such key exists, return null.
# Each operation should run in O(1) time.

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextItem = None

class LRU:
    def __init__(self, maxitems):
        self.oldestItem = None
        self.newestItem = None
        self.items = {}
        self.maxitems = maxitems

    def set(self, key, value):
        item = Item(key, value)
        if key in self.items:
            self.items.pop(key, None)

        if len(self.items) < self.maxitems:
            self.newestItem = item
            if not self.oldestItem:
                self.oldestItem = item
            self.items[key] = item
        else:
            self.newestItem = item
            self.items.pop(self.oldestItem.key, None)
            self.oldestItem = self.oldestItem.nextItem
            self.items[key] = item

    def get(self, key):
        if key in self.items:
            return self.items[key].value
        else:
            return None


cache = LRU(2)
cache.set("a", "5")
# cache.set("a","4")
cache.set("b", "2")
cache.set("c", "3")
print(cache.get("a"))