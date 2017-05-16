# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.dp = {}
        if len(prices) <= 1:
            return 0
        # buy = None
        # return self._impl_dp_(prices, buy, 0)
        # return self._impl_iterative_(prices)
        return self.linear_programming(prices)


    '''
    The complexity is N, I have to iterate the p to figure all the best of bests from each p
    '''

    def linear_programming(self, p):
        # print(p)
        buy, sell = p, p
        min_buy = self.argmin(buy)
        if min_buy is None:
            tmp = []
        elif min_buy == len(p)-1:
            tmp = []
        else:
            tmp = sell[min_buy:]
        max_sell = self.argmax(tmp, min_buy)


        cur = 0
        while True:
            pass








        print(min_buy, max_sell, p, tmp)
        if min_buy is None or max_sell is None:
            if min_buy is None and max_sell is None:
                return 0
            elif min_buy is None:
                del sell[max_sell]
                return self.linear_programming(sell)
            else:
                del buy[min_buy]
                return self.linear_programming(buy)
        # print(buy[min_buy], sell[max_sell])
        return max(sell[max_sell] - buy[min_buy], 0)


    def argmax(self, v, offset=0):
        # print(v.index(max(v))+offset)

        if not len(v):
            return None
        return v.index(max(v))+offset

    def argmin(self, v, offset=0):
        # print(v)
        if not len(v):
            return None
        return v.index(min(v))+offset

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

if __name__ == "__main__":
    test = Solution()
    # p = [7, 1, 5, 3, 6, 4]
    p = [7, 6, 4, 3, 1]
    p = [3,2,6,5,0,3]
    # p = [2,4,1]
    # p = [7, 6, 4, 3, 1]
    ret = test.maxProfit(p)
    print(ret)