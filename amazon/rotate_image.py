class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return []
        for i in range(len(matrix)//2): # symmetric, so half
            r = len(matrix) - i - 1
            for j in range(i, len(matrix)-i-1): # don't include the last point, because the first point is swapped with the last point
                matrix[i][j], matrix[j][r], matrix[-j-1][i], matrix[r][-j-1] = matrix[-j-1][i], matrix[i][j], matrix[r][-j-1], matrix[j][r]




t = Solution()
matrix = [[1,2],[3,4]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
t.rotate(matrix)
print(matrix)