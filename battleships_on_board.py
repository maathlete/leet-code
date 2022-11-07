class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        m, n =  len(board), len(board[0])
        
        visited = set()
        
        neighbors = {(-1, 0), (0, 1), (1, 0), (0, -1)}
        
        def dfs(i, j):
            
            visited.add((i, j))
            
            for dx, dy in neighbors:
                
                if 0 <= i + dx < m and 0 <= j + dy < n and (i+dx, j+dy) not in visited and board[i+dx][j+dy] == "X":
                    
                    dfs(i+dx, j+dy)
        
        battleships = 0
        
        for i in range(m):
            
            for j in range(n):
                
                if (i, j) not in visited and board[i][j] == "X":
                    
                    dfs(i, j)
                    
                    battleships += 1
            
        
        return(battleships)
