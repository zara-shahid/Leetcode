class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = Counter(nums)

        points = [0] * (max(nums) + 1)
        for val in s:
            points[val] = val * s[val]

        prev1 = 0
        prev2 = 0

        for i in range(len(points)):
            curr = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = curr

        return prev1
