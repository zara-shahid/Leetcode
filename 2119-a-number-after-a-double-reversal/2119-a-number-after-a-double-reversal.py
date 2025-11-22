class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True
        last_dig=num%10
        if last_dig==0:
            return False
        return True
        