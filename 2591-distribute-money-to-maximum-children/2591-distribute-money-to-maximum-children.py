class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        
        left = money-children
        ans = min(left//7,children)
        after_8 = left - ans*7
        rem_child = children - ans
        if after_8 == 3 and rem_child == 1:
            ans-=1
        if ans == children and left != ans * 7:
            ans -= 1
        return ans
