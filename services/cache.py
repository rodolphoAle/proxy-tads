from collections import OrderedDict
import time

CACHE_TTL_SECONDS = 300

class Cache:
    def __init__(self, capacity=1000, ttl=CACHE_TTL_SECONDS):
        self.capacity = capacity
        self.ttl = ttl
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        value, timestamp = self.cache[key]
        # Verifica o TTL
        if (time.time() - timestamp) > self.ttl:
            del self.cache[key]
            return None
        self.cache.move_to_end(key)
        return value

    def put(self, key, value):
        self.cache[key] = (value, time.time())
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

_cache_instance = None

def get_cache():
    global _cache_instance
    if _cache_instance is None:
        _cache_instance = Cache()
    return _cache_instance