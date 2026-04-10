from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        j = 0
        radius = 0
        
        for house in houses:
            
            while j < len(heaters) - 1 and house > (heaters[j] + heaters[j + 1]) / 2:
                j += 1
            
            distance = abs(house - heaters[j])
            radius = max(radius, distance)
        
        return radius