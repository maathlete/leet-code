#Question: https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        n = len(num)
        expressions = set()

        def backtrack(i, path, previous=None, value=0):

            if i == n and value == target:

                expressions.add(path)

            else:

                for j in range(i+1, n+1):

                    new = int(num[i:j])

                    if (j == i + 1) or (j > i + 1 and num[i] != '0'):

                        if previous is None:

                            backtrack(j, num[i:j], new, new)

                        else:

                            backtrack(j, path + '+' + num[i:j], new, value + new)
                            backtrack(j, path + '-' + num[i:j], -new, value - new)
                            backtrack(j, path + '*' + num[i:j], previous*new, value - previous + previous*new)

        backtrack(0, '')

        return(list(expressions))
