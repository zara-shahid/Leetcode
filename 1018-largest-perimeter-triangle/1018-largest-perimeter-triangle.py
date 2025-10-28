class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        num_sort=sorted(nums,reverse=True)
        for i in range(len(num_sort) - 2):
            a = num_sort[i]
            b = num_sort[i + 1]
            c = num_sort[i + 2]
            if b+c>a:
                return a+b+c
        return 0

        