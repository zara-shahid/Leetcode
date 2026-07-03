class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        arr = []
        seen = {}

        for i in range(len(nums)):
            num = nums[i]

            if seen.get(num, 0) < k:
                arr.append(num)
                seen[num] = seen.get(num, 0) + 1

        return arr