1# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:20:20 2021

@author: aaaro
"""

# there are N oranges
# Each day, you can choose from one of the following actions:
    # 1. Eat 1 orange
    # 2. If N % 2 == 0, you can eat N/2 oranges
    # 3. If N % 3 == 0, you can eat 2N/3 oranges
# Return the minimum number of days to eat N oranges
import functools

#optimized DFS solution
#with @functools.lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        
        @functools.lru_cache(None)
        def mindays(n):
            if n == 0:
                return(0)

            if n == 1:
                return(1)

            else:
                return(1 + min(n%3 + mindays(n//3), n%2 + mindays(n//2)))
            
        return(mindays(n))

#depth-first search
def mindays(n):
    
    if n <= 0:
        return(0)
    
    if n == 1:
        return(1)
    
    else:
        
        options = []
                
        v1 = 1 + mindays(n-1)
        options.append(v1)
        
        if n%2 == 0:
            v2 = 1 + mindays(n-(n/2))
            options.append(v2)
            
        if n%3 == 0:
            v3 = 1 + mindays(n-(2*n/3))
            options.append(v3)
        
        return(min(options))
            