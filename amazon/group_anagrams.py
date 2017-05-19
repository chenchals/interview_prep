class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hist = dict()
        # first round, build letter set
        letter_set = set()
        for each_str in strs:
            for s in each_str:
                letter_set.add(s)
        for each_str in strs:
            this_hist = dict(zip(letter_set, [0 for _ in range(len(letter_set))]))
            for s in each_str:
                this_hist[s] += 1
            hashale = ''.join([str(x) for x in list(this_hist.values())])
            # print(hashale, each_str)
            if hashale in hist:
                hist[hashale].append(each_str)
            else:
                hist[hashale] = [each_str]
        # print(hist)
        ret = []
        for key in hist:
            ret.append(hist[key])
        return ret
        # second round, build the histogram




t = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
ret = t.groupAnagrams(input)
print(ret)