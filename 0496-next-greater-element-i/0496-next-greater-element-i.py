class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if not stack:
                result[nums2[i]]=-1
            else:
                result[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        return [result[num] for num in nums1]

                

        