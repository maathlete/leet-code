class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factors = [1, n]
        
        for i in range(2, n//2 + 1):
            
            if (n % i == 0):
                
                factors.append(i)
                factors.append(n//i)
                
        factors = sorted(list(set(factors)))
        
        if k > len(factors):
            return(-1)
        
        else:
            return(factors[k - 1])
