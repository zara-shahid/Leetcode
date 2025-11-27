class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def convert(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month-1]) + day
        
        startA=convert(arriveAlice)
        endA=convert(leaveAlice)
        startB=convert(arriveBob)
        endB=convert(leaveBob)

        start=max(startA,startB)
        end=min(endA,endB)

        if end<start:
            return 0

        return end-start+1