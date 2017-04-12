class Vertex(object):
	def __init__(self, x, distance):
		# 2-dim tuple (x, y)
		self.key = x
		# distance[(1,2)] = distance -> coord to cost dict
		self.distance = distance
		self.parent = None




def Dijkstra(graph, start, end):
	# set of visited coord
	for i in range(len(graph)):
		for j in range(len(graph[0])):
			neighbour_list = [(i+1, j), (i-1,j), (i,j-1), (i, j+1)]
			for coord in neighbour_list:
				x, y = coord
				if x < 0 or y < 0:
					continue