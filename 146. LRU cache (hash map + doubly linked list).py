class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.lru = None
        self.mru = None

    def updateKeyToMRU(self, key: int):
        if self.size == 1: return
        if self.map[key] is self.mru: return
        if self.map[key] is self.lru:
            self.lru = self.lru.next
            self.lru.prev = None
        else:
            self.map[key].prev.next = self.map[key].next
            self.map[key].next.prev = self.map[key].prev
        self.map[key].prev = self.mru
        self.mru.next = self.map[key]
        self.mru = self.map[key]
        self.mru.next = None

    def get(self, key: int) -> int:
        if key in self.map:
            if self.size == 1: return self.map[key].value
            self.updateKeyToMRU(key)
            return self.map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.updateKeyToMRU(key)
            return
        if self.size < self.capacity:
            self.map[key] = Node(key, value, prev=self.mru)
            self.size += 1
            if self.size == 1:
                self.mru = self.map[key]
                self.lru = self.mru
            else:
                self.mru.next = self.map[key]
                self.mru = self.map[key]
            return
        else:
            # self.size == self.capacity

            if self.size == 1:
                # clear variables
                del self.map[self.lru.key]
                self.lru = None
                self.mru = None
                self.size = 0
            else:
                # remove LRU
                del self.map[self.lru.key]
                self.lru = self.lru.next
                self.lru.prev = None
                self.size -= 1

            # add new value
            self.put(key, value)

["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

cache = LRUCache(capacity=3)

cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
print(cache.get(4))
print(cache.get(3))
print(cache.get(2))
print(cache.get(1))
cache.put(5, 5)
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
print(cache.get(4))
print(cache.get(5))