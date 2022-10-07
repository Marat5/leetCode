# class MyCalendar:
#     def __init__(self):
#         self.events = []

#     def book(self, start: int, end: int) -> bool:
#         for (e_start, e_end) in self.events:
#             if start < e_end and end > e_start:
#                 return False

#         self.events.append((start, end))
#         return True

# Solution with binary search and keeping the array sorted
class MyCalendar:
    def __init__(self) -> None:
        self.events = []

    def book(self, start: int, end: int) -> bool:
        left = 0
        right = len(self.events)
        if right == 0:
            self.events.append((start, end))
            return True

        while left < right:
            mid = (left + right) // 2
            if self.events[mid][1] <= start:
                left = mid + 1
            else:
                right = mid

        if left == len(self.events):
            self.events.append((start, end))
            return True
        if self.events[left][0] >= end:
            self.events.insert(left, (start, end))
            return True

        return False


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
test = [[97, 100], [33, 51], [89, 100], [83, 100], [75, 92], [76, 95], [19, 30], [53, 63], [8, 23], [
    18, 37], [87, 100], [83, 100], [54, 67], [35, 48], [58, 75], [70, 89], [13, 32], [44, 63], [51, 62], [2, 15]]
for s, e in test:
    print(obj.book(s, e))
