from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        maxDeque = deque()

        minDeque = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()
            minDeque.append(right)

            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:

                if maxDeque[0] == left:
                    maxDeque.popleft()

                if minDeque[0] == left:
                    minDeque.popleft()

                left += 1

            ans += right - left + 1

        return ans