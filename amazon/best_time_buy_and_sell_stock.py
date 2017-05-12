# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.dp = {}
        buy = None
        if len(prices) <= 1:
            return 0
        # return self._impl_dp_(prices, buy, 0)
        return self._impl_iterative_(prices)

    def _impl_iterative_(self, p):
        p = list(p)
        best = max(p[1] - p[0], 0)
        best_buy = p[0]
        for i in p[1:]:
            if i > best_buy:
                best = max(i-best_buy, best)
            else:
                best_buy = i
            # if i - best_buy > best:
            #     best = i - best_buy
            # else:
            #     best_buy = i
        return best

    def _impl_dp_(self, p, buy, pos):
        if pos == len(p)-1:
            if buy:
                return p[pos]-buy
            else: # never reach this condition
                return 0
        '''
        1. if buy:
            1.1 sell and store this profit, compare this with 1.2
            1.2 wait until next round
        2. if not buy:
            2.1 buy
            2.2 wait
        '''
        if buy:
            # already purchased
            # sell
            left = p[pos] - buy
            # wait
            if (buy, pos+1) not in self.dp:
                right = self._impl_(p, buy, pos+1)
            else:
                right = self.dp[(buy, pos+1)]
            # print(left, right)
            return max(left, right)
        else:
            # don't buy:
            # buy
            if (p[pos], pos+1) not in self.dp:
                left = self._impl_(p, p[pos], pos+1)
            else:
                left = self.dp[(p[pos], pos+1)]
            # wait
            if (None, pos+1) not in self.dp:
                right = self._impl_(p, None, pos+1)
            else:
                right = self.dp[(None, pos+1)]
            return max(left, right)

# if __name__ == "__main__":
#     test = Solution()
#     p = [7, 1, 5, 3, 6, 4]
#     # p = [7, 6, 4, 3, 1]
#     ret = test.maxProfit(p)
#     print(ret)