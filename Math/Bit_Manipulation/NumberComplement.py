import math

def findComplement(num: int) -> int:
        # Find the number which can make it possible to complement num
        #Just by getting the length of the num and create a number
        #that has the same length and all the bits should be 1
        N: int =  int(math.log(num) / math.log(2)) + 1

        mask: int = (1 << N) - 1

        return num ^ mask


print(findComplement(3))