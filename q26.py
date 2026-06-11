from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def solve(i, j):
            if j == len(p):
                return i == len(s)
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                skip = solve(i, j + 2)
                take = match and solve(i + 1, j)
                return skip or take
            
            if match:
                return solve(i + 1, j + 1)
            
            return False
            
        return solve(0, 0)
