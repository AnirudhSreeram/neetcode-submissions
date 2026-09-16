class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = 0
        ri = len(matrix) - 1
        while li <= ri:
            mi = (li + ri) //2
            if target > matrix[mi][-1]:
                li = mi + 1
            elif target < matrix[mi][0]:
                ri = mi - 1
            else:
                break
        
        if not (li <= ri):
            return False
        row = (li + ri) // 2
        l = 0
        r = len(matrix[row]) -1
        while l <= r:
            m = (l + r) //2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False


