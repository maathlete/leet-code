# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:54:39 2021

@author: aaaro
"""

calculated = {}

def fibonacci(n):
    if n == 0:
        return(0)
    
    elif n == 1:
        return(1)
    
    elif n in calculated:
        return(calculated[n])
    
    else:
        calculated[n] = fibonacci(n-1) + fibonacci(n-2)
        return(calculated[n])


fibonacci(5)    