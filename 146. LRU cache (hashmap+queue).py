class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache[key]["occurrences"] += 1
            self.queue.append(key)
            return self.cache[key]["value"]
        return -1

    def put(self, key: int, value: int) -> None:
        self.queue.append(key)
        # key is already in cache
        if key in self.cache:
            self.cache[key] = {"value": value, "occurences": self.cache[key]["occurrences"]+1}
            return

        # key is not in cache
        self.cache[key] = {"value": value, "occurrences": 1}
        self.size += 1

        if self.size > self.capacity:
            done = False
            while not done:
                lru = self.queue.pop(0)
                self.cache[lru]["occurrences"] -= 1
                if self.cache[lru]["occurrences"] == 0:
                    del self.cache[lru]
                    done = True
            self.size -= 1

cache = LRUCache(capacity=2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))