class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first = len(a) - 1
        sec = len(b) - 1
        carry = 0
        result = []

        while first >= 0 or sec >= 0 or carry > 0:
            first_1 = int(a[first]) if first >= 0 else 0
            sec_2 = int(b[sec]) if sec >= 0 else 0
            total = first_1 + sec_2 + carry
            digit = total % 2
            carry = total // 2
            result.append(str(digit))
            first -= 1
            sec -= 1

        return "".join(result[::-1])
