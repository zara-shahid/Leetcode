class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += 2**32

        digits = "0123456789abcdef"
        res = ""

        while num > 0:
            res = digits[num % 16] + res
            num //= 16

        return res
