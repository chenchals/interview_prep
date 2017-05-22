class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        horizontal = len(matrix[0])-1
        vertical = 0
        while horizontal >= 0 and vertical < len(matrix):
            if matrix[vertical][horizontal] == target:
                return True
            elif matrix[vertical][horizontal] < target:
                vertical += 1
            elif matrix[vertical][horizontal] > target:
                horizontal -= 1
            else:
                raise  Exception('unknown issue, should never reach to this line')
        return False


t = Solution()
inputs = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
ret = t.searchMatrix(inputs, 19)
print(ret)