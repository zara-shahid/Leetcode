class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        n=len(arr)
        for i in range(len(arr)):
            total+=arr[i]*(((i+1)*(n-i)+1)//2)
        return total


        