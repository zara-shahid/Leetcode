class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common_el=set(nums1) & set(nums2)
        if not common_el:
            return -1
        return min(common_el)
        