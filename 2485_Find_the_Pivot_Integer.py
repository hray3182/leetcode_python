# https://leetcode.com/problems/find-the-pivot-integer/
class Solution:

    def pivotInteger(self, n: int) -> int:
        left = (1 + n) * n // 2 
        right = 0

        for i in range(n):
            right += i+1
            if left == right:
                return i + 1
            left -= i + 1
        return -1


print(Solution().pivotInteger(8))