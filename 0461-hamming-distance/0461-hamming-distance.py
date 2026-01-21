class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_distance = bin(x ^ y).count("1")
        return hamming_distance


        