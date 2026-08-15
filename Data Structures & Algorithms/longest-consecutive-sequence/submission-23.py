class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_map = set(nums)
        maximum=0
        for num in num_map:
            if num-1 in num_map:
                continue
            count=0
            while num in num_map:
                count+=1
                num+=1
            if count>maximum:
                maximum = count
        return maximum
            
        
        