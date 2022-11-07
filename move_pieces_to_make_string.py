class Solution:
    
    def bf_dfs(self, start, target):
        
        memo = {}
        
        def dfs(i, start):
            
            key = ''.join(start)
            
            if i == n:
                                                            
                return(True if key == target else False)
            
            answer = False
            
            if start[i] == "_":
                
                answer |= dfs(i+1, start)
            
            elif start[i] == 'L':
                
                if i > 0 and start[i - 1] == "_":
                    
                    start[i-1] = "L"
                    start[i] = "_"
                    
                    answer |= dfs(i + 1, start)
                    
                answer |= dfs(i + 1, start)
            
            else:
                
                if i < n  - 1 and start[i + 1] == "_":
                    
                    start[i+1] = "R"
                    start[i] = "_"
                    
                    answer |= dfs(i + 1, start)
                    
                answer |= dfs(i + 1, start)
                                                        
            return(answer)
        
        return(dfs(i=0, start=list(start)))
    
    def canChange(self, start: str, target: str) -> bool:
        
        i, j = 0, 0
        
        while i < len(start) and j < len(target):
            
            while i < len(start) and start[i] == "_":
                i += 1
            
            while j < len(target) and target[j] == "_":
                j += 1
                
            if i < len(start) and j < len(target) and start[i] != target[j]:
                return(False)
            
            if i < len(start) and j < len(target) and start[i] == "R" and i > j:
                return(False)
            
            if i < len(start) and j < len(target) and start[i] == "L" and i < j:
                return(False)
            
            i += 1
            j += 1
            
        while i < len(start) and start[i] == "_":
            
            i += 1
            
        while j < len(target) and target[j] == "_":
            
            j += 1
        
        return(i == j)
