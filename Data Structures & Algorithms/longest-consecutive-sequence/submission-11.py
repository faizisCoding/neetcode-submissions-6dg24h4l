class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        map = {}
        for i in nums:
            map[i]=1
        for num in map.keys():
            if num-1 in map and num+1 in map:
                continue
            i=num
            #count=1
            while i+1 in map.keys():
                map[num]+=1
                i+=1
        return max(map.values())
            
        
        