class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums = sorted(nums)
        n = len(nums)
        prefix = [0] * (n + 1)
        ans = []
    
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for q in queries:
            left = 0 
            right = n

            while left <= right:
                mid = (left+right)//2

                if prefix[mid]<=q:
                    left = mid+1
                else:
                    right = mid-1
                    
            ans.append(right)
        return ans
