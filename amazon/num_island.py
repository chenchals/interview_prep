class Solution(object):
    def numIslands(self, grid, verbose=False):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 0, 1, x
        count = 0
        stack = list()
        for i in range(len(grid)):
            grid[i] = list(grid[i])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'x' or grid[i][j] == '0':
                    continue
                if grid[i][j] == '1':
                    count += 1
                stack.append((i, j))
                grid[i][j] = 'x'
                while len(stack) != 0:
                    x, y = stack.pop(0)
                    # check left
                    if grid[max(x - 1, 0)][y] == '1':
                        stack.append((max(x - 1, 0), y))
                        grid[max(x - 1, 0)][y] = 'x'
                    # check right
                    if grid[min(x + 1, len(grid) - 1)][y] == '1':
                        stack.append((min(x + 1, len(grid) - 1), y))
                        grid[min(x + 1, len(grid) - 1)][y] = 'x'
                    # check up
                    if grid[x][max(y - 1, 0)] == '1':
                        stack.append((x, max(y - 1, 0)))
                        grid[x][max(y - 1, 0)] = 'x'
                            # check down
                    if grid[x][min(y + 1, len(grid[0]) - 1)] == '1':
                        stack.append((x, min(y + 1, len(grid[0]) - 1)))
                        grid[x][min(y + 1, len(grid[0]) - 1)] = 'x'

        return count



test = Solution()
input_graph = ["11000", "11000", "00100", "00011"]
print(input_graph)
ret = test.numIslands(input_graph, verbose=True)
print(ret)