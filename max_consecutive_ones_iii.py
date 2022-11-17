#relevant questions:
  # ii: https://leetcode.com/problems/max-consecutive-ones-ii/description/
  # iii: https://leetcode.com/problems/max-consecutive-ones-iii/description/
  
# great sliding window practice set

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
      
        l, r = 0, 0
        
        max_consec_ones = float('-inf')

        num_zeros = 0

        while r < n:

            if nums[r] == 0:

                num_zeros += 1

            while num_zeros == k + 1:

                if nums[l] == 0:

                    num_zeros -= 1

                l += 1

            max_consec_ones = max(max_consec_ones, r - l + 1)

            r += 1

        return(max_consec_ones)
