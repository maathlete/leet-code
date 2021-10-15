#binary search approach to find the number i s.t. i**2 <= x and i+1 > x

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return(0)
        
        elif x <= 3:
            return(1)
        
        else:
                    
            l = 0
            r = x//2 
            
            while l <= r:
                
                m = (l + r)//2
                
                if m*m > x: 
                    r = m - 1
                    
                elif m*m < x:
                    l = m + 1
                    
                else:
                    return(m)
                
            return(min(l, r))
                







        
