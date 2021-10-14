#Sieve of Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 3:
            return(0)
        
        else:
            
            options = [1 for _ in range(2, n)]
            
            for i in range(2, int(n**1/2) + 1):
                
                if options[i - 2]: 
                    
                    j = i*i 
                    
                    while j < n:
                        
                        options[j - 2] = 0
                        
                        j += i
            
            return(sum(options))
                        
                