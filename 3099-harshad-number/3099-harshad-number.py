class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res=0
        digits_list = [int(d) for d in str(x)]
        for i in range(len(digits_list)):
            res+=digits_list[i]
        if x%res==0:
            return res
        return -1
        