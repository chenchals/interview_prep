class Solution(object):
    def countPrimes(self, n):
        '''
        Fill in known non primes in array n, only check those are not been marked
        :param n:
        :return:
        '''
        if n < 2:
            return 0
        lookup = [True for _ in range(n)]
        lookup[0], lookup[1] = False, False
        # lookup.add(2)
        for i in range(2, int(n**0.5)+1):
            if not lookup[i]:
                continue
            for j in range(i, n//i+1):
                lookup[i*j] = False
        print(lookup)
        return sum(lookup)

    def isPrime(self, n):
        if n == 2:
            return True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True



    def _countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        isPrime=[1]*n
        isPrime[0]=0
        isPrime[1]=0
        for i in range(2,int(n**0.5)+1):
            for j in range(2,int(n/i)+1):
                if i*j<n:
                    isPrime[i*j]=0
        return sum(isPrime)



t = Solution()
ret = t.countPrimes(7)
print(ret)