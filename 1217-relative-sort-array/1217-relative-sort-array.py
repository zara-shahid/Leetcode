from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c_arr1=Counter(arr1)
        res=[]
        remaining=[]
        for num in arr2:
            res.extend([num]*c_arr1[num])
        for num in c_arr1:
            if num not in arr2:
                remaining.extend([num]*c_arr1[num])
        rem=sorted(remaining)
        res.extend(rem)
        return res



