# Problem Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(haystack)
        n = len(needle)

        if N < n:
            return -1

        for i in range(0, N):
            isOccur = True

            for j in range(0, n):
                if i + j < N and haystack[i + j] != needle[j]:
                    isOccur = False
                    break
            
            if isOccur and i <= N - n:
                return i

        return -1


if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"

    find = Solution()
    ans:int = find.strStr(haystack, needle)
    print(ans)