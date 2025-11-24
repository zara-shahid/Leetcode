class Solution:
    def countEven(self, num: int) -> int:
        ans=0
        digit_sum=0
        for i in range(1,num+1):
            digit_sum = sum(int(d) for d in str(i)) 
            if digit_sum%2==0:
                ans+=1
        return ans
        