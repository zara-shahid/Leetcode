class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        temp = 0  
        
        while left <= right:
            binary = bin(left)
            one_count = binary.count('1')  
            if is_prime(one_count):
                temp += 1 
            left += 1
        
        return temp
