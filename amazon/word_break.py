class Solution(object):

    def __init__(self):
        self.trie = {}




    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # build trie
        for char in s:
            # current char
            pass
        for word in wordDict:
            pass
        print(self.trie)
        # traverse s by removing sub-trie if match


        # check if trie is empty (break down to all words in dict)



t = Solution()
inputs = ['abc', 'aaa', 'abd']
ret = t.wordBreak('aa',inputs)
import pprint
pp = pprint.PrettyPrinter()
pp.pprint(ret)