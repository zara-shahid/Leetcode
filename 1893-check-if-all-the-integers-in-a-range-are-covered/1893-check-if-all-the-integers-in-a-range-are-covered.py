class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        
        while left <= right:
            covered = False

            for start, end in ranges:
                if start <= left <= end:
                    covered = True
                    break

            if not covered:
                return False

            left += 1

        return True