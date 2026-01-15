class Solution:
    def calculate(self, s: str) -> int:
        stack = []      
        ans = 0
        current_no = 0
        operator = 1     
        i = 0
        n = len(s)
        
        while i < n:
            char = s[i]
            
            if char.isdigit():
                current_no = 0
                while i < n and s[i].isdigit():
                    current_no = current_no * 10 + int(s[i])
                    i += 1
                ans += operator * current_no
                continue 
            
            elif char == '+':
                operator = 1
            
            elif char == '-':
                operator = -1
            
            elif char == '(':
                stack.append((ans, operator))
                ans = 0
                operator = 1  
            
            elif char == ')':
                prev_ans, prev_operator = stack.pop()
                ans = prev_ans + prev_operator * ans
            
            i += 1
        
        return ans
