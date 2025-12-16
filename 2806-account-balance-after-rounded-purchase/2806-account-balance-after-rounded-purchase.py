class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rounded_amount=floor((purchaseAmount+5)/10)*10
        return 100-rounded_amount
        