from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # List containing ans
        ans: List[int] = []

        i: int = 0
        while i < len(nums):
            # if index != arr[index] - 1 and if arr[arr[index]-1] doesn't have same value then swap
            if i != nums[i] - 1 and nums[nums[i] - 1] != nums[i]:
                # swap
                temp: int = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp

            else:
                i += 1
        

        # check which number is missing and add it to list
        i = 0

        while i < len(nums):
            if nums[i] - 1 != i:
                ans.append(i + 1)

            i += 1

        return ans


if __name__ == "__main__":
    find = Solution()
    arr: List[int] = [4,3,2,7,8,2,3,1]
    ans: List[int] = find.findDisappearedNumbers(arr)

    print(ans)