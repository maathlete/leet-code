#quick recursive solution

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0:
            return(False)
        
        elif n == 1: #2^0 = 1
            return(True)
        
        elif n%2 == 1: #anything with an odd factor will not be a power of 2
            return(False)
        
        else:
            return(self.isPowerOfTwo(n//2))
            
            
        
