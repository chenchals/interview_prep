from collections import deque

class Solution(object):
    def __init__(self):
        self.adj_list = {}
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if len(wordList) == []:
            return 0
        self._build_neighbour(wordList+[beginWord])
        stack = deque()
        visiting_history = dict(zip(wordList+[beginWord], [[False, None] for _ in range(len(wordList+[beginWord]))]))
        count = 0
        stack.append(beginWord)
        while len(stack) > 0:
            cur = stack.popleft()
            if visiting_history[cur][0]:
                continue
            # print(visiting_history)
            visiting_history[cur][0] = True
            neighbours = self.get_neighbours(cur)
            # if cur == 'lose':
            #     print(neighbours)
            count += 1
            for neighbour in neighbours:
                # print(neighbour, visiting_history)

                if neighbour == endWord:
                    counter = 1
                    visiting_history[neighbour][1] = cur
                    # print(neighbour, visiting_history)
                    track = cur
                    while track:
                        # print(track)
                        counter += 1
                        track = visiting_history[track][1]
                    return counter
                elif visiting_history[neighbour][0]:
                    continue
                else:
                    if neighbour not in stack:
                        stack.append(neighbour)
                        visiting_history[neighbour][1] = cur
        return 0

    def _build_neighbour(self, neighbour_list):
        for node in neighbour_list:
            if node in self.adj_list:
                continue
            self.adj_list[node] = set()
            for neighbour in neighbour_list:
                if node == neighbour:
                    continue
                else:
                    for i in range(len(node)):
                        tmp = node
                        node = list(node)
                        node[i] = neighbour[i]
                        node = ''.join(node)
                        if node == neighbour:
                            node = tmp
                            self.adj_list[node].add(neighbour)
                            continue
                        # not equal , put it back
                        node = tmp


    def get_neighbours(self, node):
        return self.adj_list[node]






t = Solution()
# ret = t.ladderLength('a', 'b', ['a','b','c'])
# ret = t.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])
# ret = t.ladderLength("hot","dog",["hot","dog","cog","pot","dot"])
ret = t.ladderLength("leet","code",["lest","leet","lose","code","lode","robe","lost"])
print(ret)
