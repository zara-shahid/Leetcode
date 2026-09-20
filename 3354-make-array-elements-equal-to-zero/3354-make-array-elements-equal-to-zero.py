class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            if nums[i] != 0:
                continue

            for direction in [-1, 1]:
                arr = nums.copy()
                curr = i

                while 0 <= curr < n:

                    if arr[curr] == 0:
                        curr += direction

                    else:
                        arr[curr] -= 1
                        direction *= -1
                        curr += direction

                if all(x == 0 for x in arr):
                    ans += 1

        return ans