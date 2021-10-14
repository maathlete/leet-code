# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:39:16 2021

@author: -
"""

#quality = [10, 20, 5]
#wage = [70, 50, 30]

#ans=$105.00

#what we want is the minimum cost per unit of quality

def min_cost_brute_force(wage, quality, k):
    n = len(quality)
    cost = float('inf')

    ratio = [w/q for w,q in zip(wage, quality)]
    
    for i in range(n):
        
        factor = ratio[i]
        prices = []
        
        for worker in range(n):
            price = factor*quality[worker]
            
            if price < wage[worker]: 
                continue
            else:
                prices.append(price)
                
        if len(prices) < k:
            continue
        else:
            prices = sorted(prices)
            
        cost = min(cost, sum(prices[:k]))
            
    return(cost)

#HEAP SOLUTION:
    #1. sorts the set of workers by cost/quality ratio asc
    #2. pushes set into minheap with negative indeces 
    
    #3. finds the minimum cost by comparing the existing cost to the cost of the k workers 
#want to maximize the quality given the cost

#
def min_cost_opt(wage, quality, k):
    import heapq #minheap
    
    cost = float('inf')
    
    workers = sorted((w/q, q, w) for q,w in zip(quality, wage))
    print(workers)
    
    pool = []
    sumq = 0
    
    for ratio, q, w in workers:
        heapq.heappush(pool, -q)
        
        sumq += q
        
        print(f'''q={q} and pool={pool} and sumq = {sumq}''')
        
        if len(pool) > k:
            sumq += heapq.heappop(pool) #returns the smallest value (e.g. value with highest quality)
            
        if len(pool) == k:
            cost = min(cost, ratio*sumq)
        
        print(f'''q={q} and pool={pool}, ratio={ratio}, sumq = {sumq}, cost = {cost}''')

    return(float(cost))

print(min_cost_opt(wage = [70, 50, 30],#, 40, 10], 
                   quality = [10, 20, 5],#, 8, 2], 
                   k = 2))

print(min_cost_brute_force(wage = [70, 50, 30], 
                           quality = [10, 20, 5], 
                           k = 2))




maxheap = [5,4,3]
minheap = [3,4,5]

    
    

