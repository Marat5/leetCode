# class MyCalendarTwo:
#     def __init__(self):
#         # Key is index, value is (start, end)
#         # Use dict for O(1) removal of the value, n
#         self.events = {}
#         self.next_index = 0

#     def book(self, start: int, end: int) -> bool:
#         # Takes O(logn) for sorting, but this solution gets time limit
#         self.events[self.next_index] = (start, end)
#         lst = []
#         for (s, e) in self.events.values():
#             lst.append((s, 1))
#             lst.append((e, -1))

#         lst.sort()
#         intersections = 0
#         for (_, one_or_minus_one) in lst:
#             intersections += one_or_minus_one
#             if intersections > 2:
#                 del self.events[self.next_index]
#                 return False
#         self.next_index += 1
#         return True

class MyCalendarTwo:
    def __init__(self) -> None:
        self.overlapping_events = []
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for (s, e) in self.overlapping_events:
            if s < end and e > start:
                return False

        for (s, e) in self.events:
            if s < end and e > start:
                self.overlapping_events.append((max(start, s), min(e, end)))

        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
test = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
for s, e in test:
    print(obj.book(s, e))
