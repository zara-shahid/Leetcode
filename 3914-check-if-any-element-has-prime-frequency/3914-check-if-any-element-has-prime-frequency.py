from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        count = Counter(nums)

        # helper function to check prime
        def prime(n: int) -> bool:
            if n <= 1:
                return False
            if n == 2:
                return True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        # check if any frequency is prime
        for fr in count.values():
            if prime(fr):
                return True
        return False
