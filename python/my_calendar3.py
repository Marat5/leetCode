class MyCalendarThree:
    def __init__(self):
        self.sorted_list_of_starts_and_ends = []
        self.max_k = 0

    def book(self, start: int, end: int) -> int:
        self.sorted_list_of_starts_and_ends.append((start, 1))
        self.sorted_list_of_starts_and_ends.append((end, -1))
        self.sorted_list_of_starts_and_ends.sort()

        intersections = 0
        for (_, one_or_minus_one) in self.sorted_list_of_starts_and_ends:
            intersections += one_or_minus_one
            self.max_k = max(self.max_k, intersections)

        return self.max_k


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))
