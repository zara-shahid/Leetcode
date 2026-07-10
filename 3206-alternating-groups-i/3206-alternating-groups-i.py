class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans=0
        n=len(colors)
        for i in range(n):
            left = (i - 1) % n
            right = (i + 1) % n
            if colors[left]!=colors[i] and colors[right]!=colors[i]:
                ans+=1
        return ans
        