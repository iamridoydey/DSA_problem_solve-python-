# Problem Link: https://leetcode.com/problems/number-of-1-bits/
def hammingWeight(n: int) -> int:
        setBits: int = 0

        while n != 0:
            if n & 1 == 1:
                setBits += 1
            
            n >>= 1
        
        return setBits


print(hammingWeight(10)) # 2