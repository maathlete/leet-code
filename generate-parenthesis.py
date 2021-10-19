class Solution:
    
     def generateParenthesis(self, N: int) -> List[str]:
            
        def dfs(n, l, current):
            
            if n == 0 and l == 0:
                results.append(current)
            
            if n > 0:
                dfs(n - 1, l + 1, current + '(')
            
            if l > 0:
                dfs(n, l - 1, current + ')')
        
        results = []
        dfs(n = N, l = 0, current = '')
        return(results)
                
        
