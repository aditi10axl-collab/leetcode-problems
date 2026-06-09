import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
       
        match = re.match(r'^[\+\-]?\d+', s)
        
        if not match:
            return 0
     
        num = int(match.group())
        
       
        return max(-2147483648, min(num, 2147483647))
      
