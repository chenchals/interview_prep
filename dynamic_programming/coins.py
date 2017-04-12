class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        solutions = [0] * (amount + 1)
        coins = sorted(coins)
        solutions[0] = 1

        return solutions[-1]


if __name__ == "__main__":
    test = Solution()
    print(list(range(6)))
    ret = test.change(10, [2,5])
    print(ret)