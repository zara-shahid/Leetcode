class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[r]+nums[l]
                if abs(target-s)<abs(target-closest):
                    closest=s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return s   
        return closest 
                    