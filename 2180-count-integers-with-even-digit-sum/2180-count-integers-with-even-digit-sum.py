class Solution:
    def countEven(self, num: int) -> int:
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum%2==0:
            return num//2
        return (num-1)//2 
        
        