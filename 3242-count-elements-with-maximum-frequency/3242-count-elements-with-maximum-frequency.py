from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_freq = max(count.values())
        ans=0
        for fr in count.values():
            if fr==max_freq:
                ans+=max_freq
        return ans


        