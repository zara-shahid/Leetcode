class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = n
        remove = 10          
        alice_turn = True
        while remove > 0:
            if stones < remove:
                return not alice_turn  
            stones -= remove
            remove -= 1
            alice_turn = not alice_turn
        return False
            

        
        