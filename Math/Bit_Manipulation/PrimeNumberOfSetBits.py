# Problem Link: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
from typing import List

def countPrimeSetBits(left: int, right: int) -> int:
        # Creating An array of 20
        primes: List[bool] = [False] * (20)
        primes[2] = primes[3] = primes[5] = primes[7] = primes[11] = primes[13] = primes[17] = primes[19] = True

        count: int = 0
        while left <= right:
            # Count number of set Bits
            bits: int = bin(left).count('1')
            if (primes[bits]):
                count += 1

            left += 1

        return count


print(countPrimeSetBits(5, 10))