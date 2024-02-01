# Problem Link: https://leetcode.com/problems/counting-bits/

from typing import List

def countBits(n: int) -> List[int]:
        # Create a list of length n + 1
        ans: List[int] = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)
        
        return ans

print(countBits(10))