class Solution:
    def partitionString(self, s: str) -> int:
        seen=set()
        count=1
        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                seen=set()
                count+=1
                seen.add(i)
        return count