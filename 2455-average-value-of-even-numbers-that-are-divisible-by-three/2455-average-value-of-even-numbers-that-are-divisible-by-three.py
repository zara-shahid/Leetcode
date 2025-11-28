class Solution:
    def averageValue(self, nums: List[int]) -> int:
        dig=[]
        for i in nums:
            if i%3==0 and i%2==0:
                dig.append(i)
        if len(dig)==0:
            return 0
        else:
            sum_dig=sum(dig)
            return sum_dig//len(dig)

        