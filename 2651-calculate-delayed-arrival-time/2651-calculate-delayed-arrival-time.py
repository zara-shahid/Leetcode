class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        twentyfour=arrivalTime+delayedTime
        if twentyfour>=24:
            return twentyfour-24
        return twentyfour
        