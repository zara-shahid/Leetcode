class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
                            
            for i in range(len(nums)):
                    if nums[i] not in path:
                        path.append(nums[i])
                        backtrack()
                        path.pop() 
        backtrack()
        return result
                    


            



        