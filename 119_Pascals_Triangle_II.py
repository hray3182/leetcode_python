from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * [rowIndex] + 1
        i = 1
        while i <= len(result) :
            result[i] = getRow(rowIndex - 1)[i-1] + getRow(rowIndex - 1)[i]  
            i += 1
        
        return result
print(Solution().getRow(6))
    