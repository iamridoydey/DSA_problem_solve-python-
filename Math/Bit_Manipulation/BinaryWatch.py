# Problem Link: https://leetcode.com/problems/binary-watch/description/
from typing import List

def readBinaryWatch(turnedOn: int) -> List[str]:
        ans: List[str] = []

        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    s = str(i) + ":"
                    if j < 10:
                        s += "0"
                    
                    s += str(j)

                    ans.append(s)
        
        return ans


print(readBinaryWatch(1))