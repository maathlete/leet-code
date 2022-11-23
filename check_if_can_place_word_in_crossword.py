#question: https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/description/

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        @functools.lru_cache(None)

        def valid_placement(i, j):

            return(0 <= i < m and 0 <= j < n and board[i][j] != "#")

        @functools.lru_cache(None)

        def dfs(i, j, k, d):

            if k == len(word):

                return(not valid_placement(i, j))

            if not valid_placement(i, j) or board[i][j] not in {' ', word[k]}:

                return(False)

            return(dfs(i + moves[d][0], j + moves[d][1], k + 1, d))

        for i in range(m):

            for j in range(n):

                for d in range(len(moves)):

                    pre_i, pre_j = i - moves[d][0], j - moves[d][1]

                    if not valid_placement(pre_i, pre_j) and dfs(i, j, 0, d):
                            
                        return(True)

        return(False)
