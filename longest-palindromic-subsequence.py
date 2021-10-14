# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:50:07 2021

@author: aaaro
"""

#case: "babad"
#   

def longestPalindrome_dp(s):
        
    n = len(s)
        
    dp = [[0 for _ in range(n)] for _ in range(n)]
        
    #set all diag values to 1
    for i in range(n):
        dp[i][i] = True
        
    #initialize max length and the starting index of the lognest pal. ss.
    maxLength = 1
    start_index = 0
        
    #runtime can be reduced by searching for all possible pairs of characters
    for i in range(n-1):
        
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start_index = i
            maxLength = 2

    #Now we search for palindromes of all possible lengths {3, ..., n}        
    for k in range(3, n+1):
            
        #when considering palindromes of size k, there are
        #       n - k + 1
        #possible indeces from which a palindrome ss of size k
        #could start
        for i in range(n - k + 1):
                
            #based on the size of the palindrome, k, this is the ending index
            #of the palindrome given the possible starting index, i
            
            j = i + k - 1
                
            #S[i][j] is a palindrome iff s[i+1:j-1] is a palindrome
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
            
                if k > maxLength:
                    maxLength = k
                    start_index = i
                    
    return(s[start_index:start_index + maxLength])

def longestPalindome_tptr(s):
    
    if len(s) == 1:
        return(s)
    
    else:
        result = s[0]
        max_length = 1
    
    for i in range(len(s)):
        
        l = i
        r = i
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            
            if r - l + 1 > max_length:
                max_length = r - l + 1
                result = s[l:r]
            
            l -= 1
            r += 1
                
            
        l = i
        r = i + 1
        
        while l > 0 and r < len(s) and s[l] == s[r]:
            
            if r - l + 1 > max_length:
                max_length = r - l + 1
                result = s[l:r]
            
            l -= 1
            r += 1
    
    return(result)
            