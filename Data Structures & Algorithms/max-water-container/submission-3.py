class Solution:
    def area(self,h1,h2,width):
        return min(h1,h2)*width
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        v_max=self.area(heights[i],heights[j],j-i)
        while i<j:
            curr_area=self.area(heights[i],heights[j],j-i)
            v_max=max(curr_area,v_max)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return v_max

        