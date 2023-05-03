"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #get the len of the matrix
        n = len(matrix) #same number of rows and column.

        #change matrix
        #loop over the rows:
        for i in range(n):
            #loop over the cols, start in curr row(only swap elems in the upper triangle)
            for j in range(i, n):
                #Swap elems(i, j) and (j, i)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #loop over rows and reverse
        for row in matrix:
            row.reverse()
