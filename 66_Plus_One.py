
from typing import List

# pass: https://imgur.com/FoOg3Xq
# https://leetcode.com/problems/plus-one/

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# 解題思路: 從最後一位數檢查，若是不為9則最後一位數加一返回，否則將值改成零並往前檢查

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = len(digits) - 1 
        if digits[curr] != 9:
            digits[curr] += 1
            return digits
        while digits[curr] == 9:
            digits[curr] = 0
            if curr == 0:
                digits.insert(0, 1)
                return digits
            curr -= 1
        digits[curr] += 1
        return digits

if __name__ == "__main__":
    digits = [1,2,3]
    # should be [1,2,4]
    print(Solution().plusOne(digits))

    digits = [4,3,2,1]
    # should be [4,3,2,2]
    print(Solution().plusOne(digits))

    digits = [9]
    # should be [1,0]
    print(Solution().plusOne(digits))

    digits = [8,9,9,9]
    # should be [9,0,0,0]
    print(Solution().plusOne(digits))