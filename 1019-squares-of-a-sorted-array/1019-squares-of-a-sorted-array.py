import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=np.array(nums)
        squared_arr=arr**2
        sorted_arr=np.sort(squared_arr)
        result=sorted_arr.tolist()
        return result

        