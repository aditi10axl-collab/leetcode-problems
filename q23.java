class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign, i, total = 1, 0, 0
        
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        while i < len(s) and s[i].isdigit():
            total = total * 10 + int(s[i])
            i += 1
            
        return max(-2**31, min(total * sign, 2**31 - 1))
