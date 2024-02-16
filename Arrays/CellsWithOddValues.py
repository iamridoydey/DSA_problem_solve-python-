from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix: List[List[int]] = [[0] * n for _ in range(m)]

        for i in range(len(indices)):
            r: int = indices[i][0]
            c: int = indices[i][1]

            # Increment the row cells
            for j in range(n):
                matrix[r][j] += 1

            # Increament the column cells
            for k in range(m):
                matrix[k][c] += 1

        odds: int = 0
        
        for i in range(m):
            for j in range(n):
                if (matrix[i][j] & 1) == 1:
                    odds += 1
        
        return odds
    

if __name__ == "__main__":
    obj = Solution()
    ans: int = obj.oddCells(2, 3, [[0, 1], [1, 1]])

    print(ans)