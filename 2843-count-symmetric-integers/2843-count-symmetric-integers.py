class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        while low <= high:
            s = str(low)

            if len(s) % 2 == 0:
                mid = len(s) // 2
                first_half = s[:mid]
                second_half = s[mid:]

                sum_first = sum(int(d) for d in first_half)
                sum_second = sum(int(d) for d in second_half)

                if sum_first == sum_second:
                    count += 1

            low += 1

        return count
