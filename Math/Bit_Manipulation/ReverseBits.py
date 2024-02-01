def reverseBits(n: int) -> int:
        num: int = 0

        for i in range(31, -1, -1):
            if n == 0:
                break
            
            # Get the current bit
            bit = n & 1
            num += bit * pow(2, i)

            n >>= 1

        return num


print(reverseBits(4294967293))