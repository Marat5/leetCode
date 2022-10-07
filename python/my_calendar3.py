class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        k = 1
        for (e_start, e_end, e_k) in self.events:
            if start >= e_start and start < e_end:
                k += e_k
            elif end > e_start and end <= e_end:
                k += e_k
        self.events.append((start, end, k))
        return k


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))
