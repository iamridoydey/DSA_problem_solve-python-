# Problem Link: https://leetcode.com/problems/binary-gap/


def binaryGap(n: int) -> int:
        i: int = 0
        j: int = 0
        gap: int = 0

        while n != 0:
            bit: int = n & 1

            if bit == 1:
                gap = max(j - i, gap)

                if gap != 0:
                    i = j
            
            elif i == j and gap == 0:
                i += 1
            
            j += 1

            n >>= 1
        
        return gap


print(binaryGap(21))
