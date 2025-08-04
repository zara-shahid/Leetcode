class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            today_price=prices[i]
            yesterday_price=prices[i-1]
            if today_price>yesterday_price:
                profit+=(today_price-yesterday_price)
        return profit