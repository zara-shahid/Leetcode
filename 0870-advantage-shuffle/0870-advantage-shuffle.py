class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = sorted((val, index) for index, val in enumerate(nums2))
        ans=[0]*len(nums1)
        l=0
        r=len(nums1)-1
        for value, index in reversed(sorted_nums2):
            if nums1[r]>value:
                ans[index]=nums1[r]
                r-=1
            else:
                ans[index]=nums1[l]
                l+=1
        return ans
        