class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        new1 = ""
        new2 = ""
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                new1 += digit
            else:
                new2 += digit
        return int(new1) + int(new2)
