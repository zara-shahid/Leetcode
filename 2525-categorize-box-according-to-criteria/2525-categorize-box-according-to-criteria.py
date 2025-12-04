class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isbulky = False
        isheavy = False
        if max(length,width,height)>=10**4:
            isbulky = True
        if length*width*height >= 10**9:
            isbulky = True
        if mass>=100:
            isheavy = True
        if isbulky == True and isheavy==True:
            return "Both"
        if isbulky==False and isheavy==False:
            return "Neither"
        if isbulky==True and isheavy==False:
            return "Bulky"
        if isheavy==True and isbulky==False:
            return "Heavy"

        