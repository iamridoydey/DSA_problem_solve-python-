from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged: List[int] = self.mergedArray(nums1, nums2)

        # Get the length of the array
        N: int = len(merged)

        # Check whether N is even or odd
        evenOdd: int = N & 1

        # Half of the number
        half: int = N // 2

        if evenOdd == 0:
            # That means it is a even number. So it have two median
            return (merged[half - 1] + merged[half]) / 2
        
        return merged[half]


    
    def mergedArray (self, nums1, nums2) -> List[int]:
        # Get the length of each array
        N1: int = len(nums1)
        N2: int = len(nums2)
        N: int = N1 + N2

        # Create a N size list
        nums: List[int] = []

        # All the pointers
        i: int = 0
        j: int = 0

        while i < N1 and j < N2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1



        # Put all the remaining elments
        while i < N1:
            nums.append(nums1[i])
            i += 1

        while j < N2:
            nums.append(nums2[j])
            j += 1

        return nums
    

if __name__ == "__main__":
    nums1: List[int] = [1, 2]
    nums2: List[int] = [3, 4]

    ans = Solution()
    val:int = ans.findMedianSortedArrays(nums1, nums2)
    print(val)