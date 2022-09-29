from typing import List


class Solution:
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     if x < arr[0]:
    #         return arr[:k]
    #     elif x > arr[-1]:
    #         return arr[len(arr)-k:]

    #     l = 0
    #     r = len(arr) - 1
    #     result = []
    #     while l < r - 1 and (arr[l] <= x or arr[r] >= x):
    #         if arr[l] <= x and l + 1 < len(arr) and arr[l + 1] <= x:
    #             l += 1
    #         else:
    #             r -= 1

    #     if r - l == 2:
    #         l += 1

    #     if l == r:
    #         result.append(arr[l])
    #         l -= 1
    #         r += 1
    #         k -= 1

    #     while k > 0:
    #         k -= 1

    #         if r >= len(arr) or abs(arr[l] - x) <= abs(arr[r] - x):
    #             result = [arr[l]] + result
    #             l -= 1
    #         else:
    #             result.append(arr[r])
    #             r += 1

    #     return result

    # To use binary search we need to look for left index in it
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]

        l = 0
        r = len(arr) - k
        while l < r:
            mid = (r + l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l+k]


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))
