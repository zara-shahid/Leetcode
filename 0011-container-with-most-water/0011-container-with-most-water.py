class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        area=0
        r=len(height)-1
        while l<r:
            width=r-l
            min_h=min(height[l],height[r])
            area=max(area,width*min_h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return area



        