class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left =0 
        already_satisfied = 0
        current_extra = 0
        maximum_extra = 0

        for i in range(len(grumpy)):
            if grumpy[i]==0:
                already_satisfied+=customers[i]

        for right in range(len(customers)):
            if grumpy[right]==1:
                current_extra+=customers[right]

            if right - left + 1 > minutes:
                if grumpy[left]==1:
                    current_extra -= customers[left]
                left+=1

            if right-left+1 == minutes:
                maximum_extra = max(maximum_extra, current_extra)

        return maximum_extra+already_satisfied



         

        