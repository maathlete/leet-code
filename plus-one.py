#There are more elegant solutions but I used string manipulation

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ''
        
        for digit in digits:
            s += str(digit)
            
        s = str(int(s) + 1)
        
        return([int(i) for i in s])
        
            
            
        
        
