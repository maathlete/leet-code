#question: https://leetcode.com/problems/strictly-palindromic-number/description/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def string_base_n(n, base):

            final = ''

            kth_root = n**(1/base)

            if kth_root > 0:

                final = ['0'] * int(kth_root)

                i = len(final)

                while n > 0 and i > 0:

                    while n < base**(i - 1) and (i - 1) > 0:

                        i -= 1

                    curr = base**(i - 1)

                    final[i - 1] = str(n//curr)

                    n -= ((n//curr) * curr)

                    i -= 1

            else:

                final = [str(n)]

            return(''.join(final))

        for base in range(2, n - 2 + 1):

            str_base_n = string_base_n(n, base)

            if str_base_n != str_base_n[::-1]:

                return(False)

        return(True)
