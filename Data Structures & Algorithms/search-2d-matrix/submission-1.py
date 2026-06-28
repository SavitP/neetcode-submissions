class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0])
        while l != r:
            mid = l + (r - l) // 2
            if (matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target):
                return True
            if (matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target):
                l = mid + 1
            else:
                r = mid
        return False
        