#https://leetcode.com/problems/guess-number-higher-or-lower/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start: int = 1
        end: int = n

        while start <= end:
            mid = start + (end - start) // 2

            isSame: int = self.guess(mid)

            if isSame == -1:
                end = mid - 1
            
            elif isSame == 1:
                start = mid + 1
            else:
                return mid


    # Create this for check the result
    def guess(self, num: int) -> int:
        if num == 6:
            return 0
        elif num > 6:
            return -1
        else:
            return 1


if __name__ == "__main__":
    obj = Solution()
    ans: int = obj.guessNumber(10)
    print(ans)

        