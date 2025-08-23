class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        product1=1
        product2=1
        for i in nums[-3:]:
            product1*=i
        for v in nums[:2] + [nums[-1]]:
            product2*=v
        return max(product1,product2)

        



        