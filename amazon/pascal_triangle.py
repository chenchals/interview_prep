class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # second row
        rowIndex += 1
        if rowIndex <= 1:
            return [1]
        current_row = [1,1]
        if rowIndex == 2:
            return current_row
        for i in range(2, rowIndex):
            next_row = [current_row[j] + current_row[j+1] for j in range(len(current_row)-1)]
            next_row.append(1)
            next_row.insert(0,1)
            current_row = next_row
        return current_row


t = Solution()
inputs = 2
ret = t.getRow(2)
print(ret)