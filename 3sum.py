# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:49:45 2021

@author: aaaro
"""

def brute_force(nums):
    
    n = len(nums)
    
    solutions = []
    
    for i in range(n):
        for j in range(i + 1, n):
            
            x = nums[i]
            y = nums[j]
            z = -(x + y)
            
            if z in nums[j+1:]:
                
                if sorted([x, y, z]) not in solutions:
                    solutions.append(sorted([x, y, z]))
            
    return(solutions)


def optimized(nums):
    
    n = len(nums)
    solutions = []
    
    nums = sorted(nums)
        
    for i, val in enumerate(nums):
        
        # if we have already computed the possible solutions for an element, 
        # we skip over any new instances of that element
        if i > 0 and val == nums[i-1]:
            continue
        
        left, right = i+1, n - 1
        
        while left < right:
            
            three_sum = val + nums[left] + nums[right]
            
            # if the sum produced is larger than zero, then the right pointer is incremented down
            if three_sum > 0:
                right -= 1
            
            # if the sum produced is less than zero, then the left pointer is incremented up
            elif three_sum < 0:
                left += 1
            
            else:
                solutions.append([val, nums[left], nums[right]])
                left += 1
                
                # This ensures the second value used isn't the same as the first solution
                # the left pointer is incremented forward until a new second value is obtained 
                # e.g. a new y in [x, y, z]
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                    
    return(solutions)
                
                # [-2, -2, 0, 0, 2, 2]
                






    
                
    