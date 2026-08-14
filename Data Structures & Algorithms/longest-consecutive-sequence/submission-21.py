class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_map = set()
        for i in nums:
            num_map.add(i)
        maximum = 1
        for num in num_map:
            if num-1 in num_map:
                continue
            i=num
            count=1
            while i+1 in num_map:
                count+=1
                i+=1
            if count>maximum:
                maximum = count
        return maximum
            
        
        