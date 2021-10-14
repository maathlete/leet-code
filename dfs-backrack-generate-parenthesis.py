# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:17:24 2021

@author: aaaro
"""

class Solution():
    
    
    def generateParenthesis(self, method, N):
        
        results = []
        
        if method == 'dfs':
            
            def dfs(n, left, current):
                
                if n == 0 and left == 0:
                    results.append(current)
                    return
                
                if n > 0:
                    dfs(n - 1, left + 1, current + '(')
                
                if left > 0:
                    dfs(n, left - 1, current + ')')
            
            dfs(n = N, left = 0, current = '')
        
        elif method == 'backtrack':
            
            def backtrack(left, right, current):
                
                if len(current) == 2*N:
                    results.append(''.join(current))
                
                if left < N:
                    current.append('(')
                    backtrack(left + 1, right, current)
                    current.pop()
                
                if right < left:
                    current.append(')')
                    backtrack(left, right + 1, current)
                    current.pop()
                    
            backtrack(left = 0, right = 0, current = [])
            
        return(results)
    
Solution().generateParenthesis(method = 'backtrack', N = 4)
        
        
    