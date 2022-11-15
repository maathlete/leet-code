# question: https://leetcode.com/problems/russian-doll-envelopes/description/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))
    
        def longest_increasing_subsequence(nums):

            dp = []

            for i in range(len(nums)):

                idx = bisect.bisect_left(dp, nums[i])

                if idx == len(dp):

                    dp.append(nums[i])

                else:

                    dp[idx] = nums[i]

            return(len(dp))
            
        return(longest_increasing_subsequence(list(map(lambda x: x[1], envelopes))))
            
