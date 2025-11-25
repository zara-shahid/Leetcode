class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result=""
        for ch in s:
            num = ord(ch) - ord('a') + 1
            result += str(num)
        while k>0:
            digit_sum = sum(int(d) for d in str(result))
            result=str(digit_sum)
            k-=1
        return int(result)

        