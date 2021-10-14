# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:19:30 2021

@author: aaaro
"""
import functools

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1/x
            n = -n

        @functools.lru_cache(None)
        def mypow(x, n):
            
            if n == 0:
                return(1)
            
            elif n == 1:
                return(x)
            
            else:
                return(mypow(x, n % 2)*mypow(x, n//2)*mypow(x, n//2))
        
        return(mypow(x,n))

print(Solution().myPow(x= 8, n= 2))