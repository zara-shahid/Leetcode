class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result={}
        ans=[]
        nums1=sorted(nums)
        for i in range(len(nums1)):
            if nums1[i] not in result:
                result[nums1[i]] = i
        for num in nums:
            ans.append(result[num])
        return ans








        