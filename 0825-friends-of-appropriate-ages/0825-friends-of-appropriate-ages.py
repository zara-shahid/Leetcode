from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        l = 0
        r= 0
        total_req = 0
        for x in range(n):
            
            while l < n and ages[l] <= 0.5 * ages[x] + 7:
                l += 1
            
            while r< n and ages[r] <= ages[x]:
                r+= 1
            
            if r> l:
                total_req += (r- l - 1)
        
        return total_req