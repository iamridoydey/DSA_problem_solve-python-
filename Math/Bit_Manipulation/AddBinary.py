from typing import List

def addBinary(a: str, b: str) -> str:
        ans: List[str] = []

        i: int = len(a) - 1
        j: int = len(b) - 1
        carry: int = 0

        while i >= 0 or j >= 0:
            sum: int = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:
                sum += int(b[j])
                j -= 1

            ans.insert(0, str(sum % 2))
            carry = sum // 2
        
        # Should have carry. If it is then add it
        if carry > 0:
            ans.insert(0, str(carry))

        return "".join(ans)


print(addBinary("11", "1"))