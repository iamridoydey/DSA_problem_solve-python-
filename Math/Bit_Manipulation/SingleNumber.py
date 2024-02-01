# Problem Link: https://leetcode.com/problems/single-number/description/
from typing import List

def singleNumber(nums: List[int]) -> int:
        ans: int = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        
        return ans


print(singleNumber([4,1,2,1,2]))