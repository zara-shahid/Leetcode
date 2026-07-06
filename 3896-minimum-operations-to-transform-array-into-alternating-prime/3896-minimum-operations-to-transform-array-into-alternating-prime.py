class Solution:
    def isPrime(self, num):
        if num <= 1:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True

    def minOperations(self, nums: list[int]) -> int:
        op = 0

        for i in range(len(nums)):
            if i % 2 == 0:         
                while not self.isPrime(nums[i]):
                    nums[i] += 1
                    op += 1
            else:                   
                while self.isPrime(nums[i]):
                    nums[i] += 1
                    op += 1

        return op