class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        col = len(matrix)

        top = 0
        bottom = col - 1
        while top <= bottom:
            middle_row = (top + bottom) // 2
            if matrix[middle_row][0] > target:
                bottom = middle_row - 1
            elif matrix[middle_row][-1] < target:
                top = middle_row + 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        middle_row = (top + bottom) // 2
        left = 0
        right = row - 1

        while left <= right:
            middle = (left + right) // 2

            if middle > target:
                right = middle - 1
            elif middle < target:
                left = middle + 1
            elif middle == target:
                return True
        return False
