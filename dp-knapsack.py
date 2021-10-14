# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:06:47 2021

@author: aaaro
"""

#knapsack

#capacity = 7
#weights = [1, 2, 4, 6]
#prices = [4, 2, 4, 7]


#naive recursive:
def solveKnapsack(capacity, weights, prices, n):
    
    if n == 0 or capacity == 0:
        return(0)
    
    #case when the weight of the item exceeds the capcity of the knapsack:
    if weights[n-1] > capacity:
        return(solveKnapsack(capacity, weights, prices, n-1))
    
    # Otherwise, the current item could or could not be added in:
        #return the maximum of one of two cases
        #   (1.) the total price with the n-1th item included
        #   (2.) the total price with the n-1th item excluded
    
    else:
        return(max(prices[n - 1] + solveKnapsack(capacity - weights[n-1], weights, prices, n-1),
                   solveKnapsack(capacity, weights, prices, n-1)))
     

solveKnapsack(capacity = 7, weights = [1,2,4,7], prices = [4,2,4,7], n = len([1,2,4,6]))    

def solveKnapsackDP(capacity, weights, prices, n):
    K = [[0 for i in range(capacity+ 1)] for j in range(n+1)]
    
    for i in range(n + 1):
        for j in range(capacity + 1):
            
            K[i][j] = None

            