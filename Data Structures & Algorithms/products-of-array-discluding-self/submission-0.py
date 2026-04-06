class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod=[1]*n
        for i in range(1,n):
            prod[i]=nums[i-1]*prod[i-1]
        rightProd=1
        for i in range(n-1,-1,-1):
            prod[i]*=rightProd
            rightProd*=nums[i]
        return prod

            