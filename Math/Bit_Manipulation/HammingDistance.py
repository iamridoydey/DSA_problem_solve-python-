def hammingDistance(x: int, y: int) -> int:
        distance: int = 0

        while x > 0 or y > 0:
            # Get the first digit from x and y everytime
            xDigit: int = x & 1
            yDigit: int = y & 1

            if xDigit != yDigit:
                distance += 1
            
            x >>= 1
            y >>= 1
        
        return distance


ans = hammingDistance(1, 4)
print(ans)