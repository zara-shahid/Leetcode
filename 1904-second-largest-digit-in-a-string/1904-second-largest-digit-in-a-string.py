class Solution:
    def secondHighest(self, s: str) -> int:
        ans=set()
        for dig in s:
            if dig.isdigit():
                ans.add(int(dig))

        answer=sorted(ans, reverse=True)
        if len(answer)<2:
            return -1
        return answer[1]


        