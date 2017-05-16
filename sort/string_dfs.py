def dfs(root, board, path):
	# print(root)
	i,j = root
	copy = board
	copy[i][j] = None
	# print(path, end=',')
	if len(path) == 0:
		return True
	entry = path[0]
	# print(path)
	if len(path) == 0:
		return True
	found = False
	for neighbour in [(i-1, j), (i,j-1), (i,j+1), (i+1,j)]:
		x, y = neighbour
		if x < 0 or y < 0 or x>=len(copy) or y>=len(copy[0]):
			continue
		print('root',(i,j),'current',(x,y), copy[x][y],'entry', entry,  'path', path)
		# print()
		if entry == copy[x][y]:
			path = path[1:]
			if len(path) == 0:
				return True
			found = dfs((x, y), copy, path)
	return found
	# print('b')


class Solution(object):
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		board = [list(x) for x in board]
		entry = word[0]
		word = word[1:]
		found = False
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == entry:
					copy = list(board)
					found = dfs((i ,j),copy, word)
				if found:
					return found
		return False

if __name__ == "__main__":
	test = Solution()
	# print(test.exist(["ABCE","SFCS","ADEE"], 'ABCCED'))
	# print(test.exist(["a"], 'ab'))
	# print(test.exist(["ab", 'cd'], 'abcd'))
	# print(test.exist(['abce', 'sfcs', 'adee'], 'see'))
	print(test.exist(["ABCE","SFES","ADEE"],"ABCESEEEFS"))
