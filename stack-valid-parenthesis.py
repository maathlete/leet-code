# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:08:07 2021

@author: aaaro
"""

def validParenthesis(s):
    
    if len(s) == 0:
        return(True)
    
    elif len(s) == 1:
        return(False)
    
    elif s[0] in (')', '}', ']'):
        return(False)
    
    else:
        
        closingMap = {')':'(',\
                      ']':'[',\
                      '}':'{'}
        
        stack = []
        
        for c in s:
            
            if c in closingMap:
                if stack and stack[-1] == closingMap[c]:
                    stack.pop()
                else:
                    return(False)
            else:
                stack.append(c)
            
        if stack:
            return(False)
        else:
            return(True)