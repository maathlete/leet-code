class Solution:
    
    def bad_backtrack(self, matchsticks):
        
        n = len(matchsticks)
        
        dp = {}
        
        def backtrack(side_lengths, i):
        
            if i == n:
                
                if sum(side_lengths) == sum(matchsticks) and min(side_lengths) == max(side_lengths):
                    
                    return(True)

                else:
                    return(False)
                
            if tuple(side_lengths) in dp:
                
                return(dp[tuple(side_lengths)])
                                
            answer = False

            for j in range(i, n):

                for k in range(4):

                    side_lengths[k] += matchsticks[j]

                    answer |= backtrack(side_lengths, j + 1)

                    side_lengths[k] -= matchsticks[j]

            dp[tuple(side_lengths)] = answer

            return(answer)
            
        return(backtrack(side_lengths=[0,0,0,0], i=0))
    
    def makesquare(self, matchsticks: List[int]) -> bool:

        matchsticks.sort(reverse=True)
        
        n = len(matchsticks)

        if sum(matchsticks) < 4 or sum(matchsticks) % 4 != 0:

            return(False)

        edge = sum(matchsticks) // 4

        dp = {}
                
        def backtrack(side_lengths, i):

            if tuple(side_lengths) in dp:

                return(dp[tuple(side_lengths)])
                        
            if edge == min(side_lengths) == max(side_lengths):

                dp[tuple(side_lengths)] = True
                
                return(True)

            answer = False

            if i > n - 1 or max(side_lengths) > edge:

                dp[tuple(side_lengths)] = answer

                return(answer)

            for k in range(4):

                side_lengths[k] += matchsticks[i]

                answer |= backtrack(side_lengths, i + 1)

                side_lengths[k] -= matchsticks[i]

            dp[tuple(side_lengths)] = answer

            return(answer)
            
        return(backtrack(side_lengths=[0,0,0,0], i=0))
