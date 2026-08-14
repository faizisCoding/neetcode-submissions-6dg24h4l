class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        map = {}
        for i in nums:
            map[i]=0
        for num in map:
            if num-1 in map:
                continue
            i=num
            count=1
            while i+1 in map.keys():
                count+=1
                i+=1
            map[num]=count
        return max(map.values())
            
        
        