class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candy=set(candyType)
        n=len(unique_candy)
        m=len(candyType)//2
        mini=min(n,m)
        return mini
        

        
        