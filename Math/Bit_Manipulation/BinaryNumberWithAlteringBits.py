# Problem Link: https://leetcode.com/problems/binary-number-with-alternating-bits/

def hasAlternatingBits(n: int) -> bool:
        prev: int = n & 1
        n >>= 1

        while n != 0:
            curr: int = n & 1

            if curr == prev:
                return False
            
            prev = curr

            n >>= 1

        return True

print(hasAlternatingBits(5))