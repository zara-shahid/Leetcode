class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr1=sorted(target)
        arr2=sorted(arr)
        return arr1==arr2
        