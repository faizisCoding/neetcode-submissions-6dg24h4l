class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        map = set()
        for i in nums:
            map.add(i)
        maximum = 1
        for num in map:
            if num-1 in map:
                continue
            i=num
            count=1
            while i+1 in map:
                count+=1
                i+=1
                if count>=maximum:
                    maximum = count
        return maximum
            
        
        