class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        soln=[]
        while 1>0:
            if numbers[l]+numbers[r] == target:
                soln.append(l+1)
                soln.append(r+1)
                return soln
            elif numbers[l]+numbers[r] > target:
                r=r-1
            elif numbers[l]+numbers[r] < target:
                l=l+1


        