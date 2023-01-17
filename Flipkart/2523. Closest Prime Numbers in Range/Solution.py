class Solution:

    def closestPrimes(self, left: int, right: int) -> List[int]:

        def is_prime(n):

            if n < 2:

                return False

            for i in range(2, int(n ** 0.5) + 1):

                if n % i == 0:

                    return False

            return True

        primes = []

        for n in range(left, right + 1):

            if is_prime(n):

                primes.append(n)

        result = [-1, -1]

        min_diff = float('inf')

        for i in range(1, len(primes)):

            diff = primes[i] - primes[i - 1]

            if diff < min_diff:

                min_diff = diff

                result = [primes[i - 1], primes[i]]

        return result
