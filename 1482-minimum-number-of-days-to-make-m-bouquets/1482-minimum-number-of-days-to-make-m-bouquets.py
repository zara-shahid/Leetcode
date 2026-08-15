class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid = (left + right) // 2
            count = 0
            bouquets = 0

            for day in bloomDay:
                if day <= mid:
                    count += 1

                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0

            if bouquets >= m:
                right = mid - 1
            else:
                left = mid + 1

        return left