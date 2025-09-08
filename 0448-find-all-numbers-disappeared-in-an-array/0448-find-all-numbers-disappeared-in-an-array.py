class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen=set()
        result = []
        for i in nums:
            seen.add(i)
        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)
        return result


            
        