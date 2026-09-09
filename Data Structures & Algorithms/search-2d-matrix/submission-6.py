class Solution:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        i=0
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                return self.binary_search(matrix[i], target)
        return False