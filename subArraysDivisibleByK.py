#we want all pairs (i, j) s.t. i < j and (prefixSum[j] - prefixSum[i]) % k == 0
#this implies (prefixSum[j] % k) - (prefixSum[i] % k) == 0 
#   and thus prefixSum[j] % k == prefixSum[i] % k

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        counts = [0] * k

        result = 0
        prefixSum = 0

        for num in nums:

            prefixSum += num

            if prefixSum % k == 0:
                result += 1
            result += counts[prefixSum % k]
            counts[prefixSum % k] += 1

        return result
