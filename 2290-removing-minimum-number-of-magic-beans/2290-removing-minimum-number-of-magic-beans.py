class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans=sorted(beans)
        total=sum(beans)
        return min(total -(len(beans)-i)*beans[i] for i in range(len(beans)))
        