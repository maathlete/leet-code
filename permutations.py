# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 16:17:57 2021

@author: -
"""


#### uses backtracking to generate all permutations of a list input

def permutations(values):
    
    if len(values) == 0:
        return([])
    
    elif len(values) == 1:
        return(values)
    
    else:
        
        li = []
    
        for i in range(len(values)):
        
            starting_value = values[i]
            remaining_values = values[:i] + values[i+1:]
        
            for p in permutations(remaining_values):
            
                if type(p) == int:
                    p = [p]
            
                li.append([starting_value] + p)
        
        return(li)
    

permutations([1,2,3,4])

#123

# starting_value = [1], remaining_value = [2, 3], permute(remaining_values):
        # starting_value = [2], remaining_values = [3], permute(remaining_values):
            # RETURNS([3])
            # -> APPEND([2, 3])
        # starting_value = [3], remaining_values = [2], permute(remaining_values):
            #RETURNS([2])
            # -> APPEND([3, 2])
        # returns([[2, 3], [3, 2]])
    #LIST UPDATES -> ([[1, 2, 3], [1, 3, 2]])

# LIST: [[1, 2, 3], [1, 3, 2]]

# starting_value = [2], remaining_values = [1, 3], permute(remaining_values):
    #starting_value = [1], remaining_values = [3], permute(remaining_values):
        # RETURNS([3])
        # -> APPEND([1, 3])
    #starting_value = [3], remaining_values = [1], permute(remaining_values):
        #RETURNS([1])
        # -> APPEND([3, 1])
    #RETURNS([1, 3], [3, 1])
 #LIST UPDATES -> ([[2, 1, 3], [2, 3, 1]])
 
# LIST: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]]

# starting_value = [3], remaining_values = [1, 2], permute(remining_values):
        # starting_value = [1], remaining_values = [2], permute(remaining_values):
            # RETURNS([2])
            # -> APPEND([1, 2])
        # starting_value = [2], remaining_values = [1], permute(remaining_values):
            # RETURNS([1])
            # -> APPEND([2, 1])
    #LIST UPDATES -> [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1

1,2,3,4
1,2,4,3
1,3,2,4
1,3,4,2
1,4,2,3
1,4,3,2
2,1,3,4
2,1,4,3
2,3,1,4
2,3,4,1
2,4,1,3
2,4,3,1
3,1,2,4
3,1,4,2
3,2,1,4
3,2,4,1
3,4,1,2
3,4,2,1
4,1,2,3
4,1,3,2
4,2,1,3
4,2,3,1
4,3,1,2
4,3,2,1
    