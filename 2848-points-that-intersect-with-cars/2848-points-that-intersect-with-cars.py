class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = []

        for i in range(len(nums)):
            start = nums[i][0]
            end = nums[i][1]

            for j in range(start, end + 1):
                arr.append(j)

        return len(sorted(set(arr)))


