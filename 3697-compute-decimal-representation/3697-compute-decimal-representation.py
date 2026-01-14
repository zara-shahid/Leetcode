class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []

        for i, digit in enumerate(str(n)[::-1]):
            d = int(digit)
            if d != 0:
                ans.append(d * (10 ** i))

        return ans[::-1]
            