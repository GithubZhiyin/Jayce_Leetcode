class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        l, r = -1, len(matrix) - 1
        while l < r:
            m = l + (r - l + 1) // 2 
            if matrix[m][0] <= target:
                l = m 
            else:
                r = m - 1
        if l == -1:
            return False
        if matrix[l][0] == target:
            return True

        
        search = matrix[l]
        l, r = 0, len(search) - 1
        while l < r:
            m = l + (r - l) // 2
            if search[m] == target:
                return True
            elif search[m] < target:
                l = m + 1 
            else:
                r = m - 1
        return True if search[l] == target else False
        


        