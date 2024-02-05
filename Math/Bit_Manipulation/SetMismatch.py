# Problem Link: https://leetcode.com/problems/set-mismatch/description/
from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
        # Use cylic sort
        i:int = 0
        while i < len(nums):

            if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                # Swap
                temp: int = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
                
            else:
                i += 1

        
        # Find the missing number
        for j in range(len(nums)):
            if nums[j] != j + 1:
                return [nums[j], j + 1]
        
        # Default case
        return [-1, -1]


ans: List[int] = findErrorNums([2, 3, 2])
print(ans)