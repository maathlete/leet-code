#question: https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution:
    
    def brutforce(nums):
        
        count = 0
        
        for i in range(len(nums)):
            
            ans = 0
            
            for j in range(i, len(nums)):
                
                ans += nums[j]
                
                if ans == k:
                    
                    count += 1
                    
        return(count)
    
    def prefixsums(nums):
        
        prefixsum = [0] * (len(nums) + 1)
        
        count = 0
        
        for i in range(1, len(prefixsum)):
            
            prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
            
        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums) + 1):
                
                if prefixsum[j] - prefixsum[i] == k:
                    
                    count += 1
                    
        return(count)
        
    
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        
        hashmap = collections.defaultdict(int)
        
        hashmap[0] = 1
        
        cumsum = 0
        
        for i in range(len(nums)):

            cumsum += nums[i]
            
            if cumsum - k in hashmap:
                
                count += hashmap[cumsum - k]
                
            hashmap[cumsum] += 1

        return(count)
