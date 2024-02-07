# Problem Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        self.sort(arr, 0, len(arr) - 1)
        return arr


    def sort(self, arr: List[int], start: int, end: int) -> None:
        # Base condition 
        if start == end:
            return
        
        
        # Get half length of the array
        mid: int = start + (end - start) // 2

        # Sort the left part of the array
        self.sort(arr, start, mid)

        # Sort the right part of the array
        self.sort(arr, mid + 1, end)

        # Merge this two array
        self.merge(arr, start, mid, mid + 1, end)


    def merge(self, arr: List[int], start1: int, end1: int, start2: int, end2: int) -> None:
        
        # Merged array
        merged: List[int] = []

        # Create two pointers for this two array
        i: int = start1
        j: int = start2

        while i <= end1 and j <= end2:
            x: int = self.setBits(arr[i])
            y: int = self.setBits(arr[j])

            if x == y:
                # If the ith element is bigger than jth element then 
                # sort them in ascending order
                if (arr[i] > arr[j]):
                    merged.append(arr[j])
                    j += 1
                else:
                    merged.append(arr[i])
                    i += 1


            elif x < y:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1

        
        # Put all the remaining elements in the merged array
        while i <= end1:
            merged.append(arr[i])
            i += 1

        while j <= end2:
            merged.append(arr[j])
            j += 1

        # Replace the arr elment with the merged array element in correct position
        for i in range(len(merged)):
            arr[start1 + i] = merged[i]


    def setBits(self, num: int) -> int:
        return bin(num).count("1")
    

if __name__ == "__main__":
    arr: List[int] = [1024,512,256,128,64,32,16,8,4,2,1]
    obj = Solution()
    obj.sortByBits(arr)
    print(arr)