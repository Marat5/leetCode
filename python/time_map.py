from collections import defaultdict


class TimeMap:
    def __init__(self):
        # Key is key, value is array of tuples [(value, timestamp)] where timestamp increases
        self.timestamps = defaultdict(lambda: [])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timestamps[key] or self.timestamps[key][0][1] > timestamp:
            return ""

        for (v, t) in reversed(self.timestamps[key]):
            if t <= timestamp:
                return v

    # Binary search has O(logn) time complexity but actually takes longer to pass test cases
    # def get(self, key: str, timestamp: int) -> str:
    #     if not self.timestamps[key] or self.timestamps[key][0][1] > timestamp:
    #         return ""

    #     searching_array = self.timestamps[key]
    #     l = 0
    #     r = len(searching_array)
    #     while l < r:
    #         mid = (l + r) // 2

    #         if searching_array[mid][1] == timestamp:
    #             return searching_array[mid][0]
    #         elif searching_array[mid][1] < timestamp:
    #             l = mid + 1
    #         else:
    #             r = mid

    #     return searching_array[r - 1][0]


o = TimeMap()
o.set("love", "high", 10)
o.set("love", "low", 20)

print(o.get("love", 5))
print(o.get("love", 10))
print(o.get("love", 15))
print(o.get("love", 20))
print(o.get("love", 25))
