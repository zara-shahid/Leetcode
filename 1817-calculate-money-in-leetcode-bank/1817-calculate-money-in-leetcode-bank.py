class Solution:
    def totalMoney(self, n: int) -> int:
        week = n // 7         
        days = n % 7           
        sum_weeks = week * (28 + (28 + (week - 1) * 7)) // 2
        sum_days = days * (2 * (week + 1) + (days - 1)) // 2
        
        return sum_weeks + sum_days