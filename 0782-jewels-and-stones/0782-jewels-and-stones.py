class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        l=list(stones)
        for i in l:
            if i in jewels:
                ans+=1
        return ans


        