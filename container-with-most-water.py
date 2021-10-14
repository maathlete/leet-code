# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:09:53 2021

@author: aaaro
"""

def max_area_brute_force(heights):
    
    n = len(heights)
    
    if n == 2:
        return(min(heights))
    
    area = [[0 for _ in range(n)] for _ in range(n)]
    
    coords = [(x+1, h) for x, h in enumerate(heights)]
    
    max_area = 1
    
    for i in range(n):
        for j in range(i+1, n):
            
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            
            area[i][j] = min(y1, y2)*(x2 - x1)
            
            if area[i][j] > max_area:
                max_area = area[i][j]
    
    return(max_area)

def max_area_optimized(heights):
    
    n = len(heights)
    
    if n == 2:
        return(min(heights))
    
    l = 0
    r = n - 1
    
    max_area = 1
    
    while l < r:
        
        area = min(heights[l], heights[r])*(r - l)
        max_area = max(area, max_area)
            
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return(max_area)
    
    