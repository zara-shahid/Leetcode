class Solution:
    def averageValue(self, nums: List[int]) -> int:
        three_dig=[]
        for i in nums:
            if i%3==0 and i%2==0:
                three_dig.append(i)
        if len(three_dig)==0:
            return 0
        else:
            sum_dig=sum(three_dig)
            return sum_dig//len(three_dig)

        