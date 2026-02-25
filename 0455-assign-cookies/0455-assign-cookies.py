class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child,cookies=0,0
        while child<len(g) and cookies<len(s):
            if s[cookies]>=g[child]:
                child+=1
            cookies+=1
        return child

        

        