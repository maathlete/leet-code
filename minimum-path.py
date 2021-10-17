# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:42:07 2021

@author: aaaro
"""

def minPathSum(self, grid):
        
    m = len(grid)
    n = len(grid[0])
    
    def dfs(i, j, memo):
        
        #Have we been here before?
        if (i, j) in memo:
            return(memo[(i, j)])
        
        #Have we reached the final square?
        if i == m - 1 and j == n - 1:
            return(grid[i][j])

        #we can ONLY move right     
        if i == m - 1:
            memo[(i, j)] = grid[i][j] + dfs(i, j + 1, memo)
            return(memo[(i, j)])
        
        #we can ONLY move down
        if j == n - 1: 
            memo[(i, j)] = grid[i][j] + dfs(i + 1, j, memo)
            return(memo[(i, j)])

        memo[(i, j)] = min(grid[i][j] + dfs(i + 1, j, memo), grid[i][j] + dfs(i, j + 1, memo))
        
        return(memo[(i, j)])
                    
    return(dfs(0, 0, {}))
