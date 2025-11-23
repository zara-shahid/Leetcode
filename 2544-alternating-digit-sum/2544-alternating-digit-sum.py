class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans=0
        for i, digit in enumerate(str(n)):
            if i%2==0:
                ans+=int(digit)
            else:
                ans-=int(digit)
        return ans

        