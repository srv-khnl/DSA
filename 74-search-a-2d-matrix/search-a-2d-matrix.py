class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows*cols-1
        while(low<=high):
            
            mid= low + (high-low)//2
            row = mid // cols
            col = mid % cols

            midvalue= matrix[row][col]

            if midvalue ==target:
                return True
            elif midvalue<target:
                low = mid+1
            else:
                high= mid-1
        return False