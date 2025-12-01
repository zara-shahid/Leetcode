class Solution:
    def countDigits(self, num: int) -> int:
        if len(str(num))==1:
            return 1
        ans=0
        for i in str(num):
            if num%int(i)==0:
                ans+=1
        return ans
        