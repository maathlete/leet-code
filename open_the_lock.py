#question: https://leetcode.com/problems/open-the-lock/description/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)

        def update_lock(state, slot, direction):

            curr = int(state[slot])

            if curr + direction < 0:

                new = '9'

            else:

                new = str((curr + direction) % 9)

            new_state = state[:slot] + new + state[slot+1:]

            return(new_state)

        def bfs(target):

            queue = [(0, '0000')]

            seen = set([0])

            min_steps = float('inf')

            while queue:

                steps, curr_state = queue.pop(0)

                if curr_state == target:

                    min_steps = min(min_steps, steps)

                    continue

                else:
                    
                    for i in range(4):

                        for dx in {-1, 1}:

                            new_state = update_lock(curr_state, i, dx)

                            if new_state not in seen and new_state not in deadends:

                                seen.add(new_state)

                                queue.append((steps + 1, new_state))

                            else:

                                continue

            return(min_steps if min_steps < float('inf') else -1)

        if '0000' in deadends:

                return(-1)
        
        else:
            
            return(bfs(target))
