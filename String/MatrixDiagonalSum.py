from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum: int = 0
        N: int = len(mat) if len(mat) < len(mat[0]) else len(mat[0])

        for i in range(N):
            sum += mat[i][i]
        
        j: int = 0
        for i in range(N - 1, -1, -1):
            sum += mat[j][i]
            j += 1
        
        # Removing common cell number if the lenth is even
        rLen = len(mat)
        cLen = len(mat[0])
        if rLen > 1 and rLen == cLen and rLen & 1 == 1 and cLen & 1 == 1:
            sum -= mat[N//2][N//2]
        


        return sum
    


if __name__ == "__main__":
    obj = Solution()
    mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
    
    ans = obj.diagonalSum(mat)

    print(ans)