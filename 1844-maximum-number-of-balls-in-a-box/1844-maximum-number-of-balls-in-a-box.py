class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_counts = {}
        for ball in range(lowLimit, highLimit + 1):
            box_number = sum(int(digit) for digit in str(ball))
            box_counts[box_number] = box_counts.get(box_number, 0) + 1
        return max(box_counts.values())
