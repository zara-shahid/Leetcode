class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        while remaining > 1:
            if (left_to_right == True) or (left_to_right == False and remaining%2!=0):
                head+=step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
        return head






        