# pass: https://imgur.com/i9HvlDk
# https://leetcode.com/problems/add-binary/description/

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# 解題思路: 先新增一個 result 變數儲存結果
# 兩數的最右邊開始遍歷，並使用一個 carry 變數來儲存進位，
# 將3數相加，並取 %2 的餘數 0 or 1 並新增到 result
# 最後返回 reuslt 的 reverse就行

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 
        i = len(a) -1
        j = len(b) -1
        result = []
        while i >= 0 or j >= 0 or carry > 0:
            curr = 0 
            if i >= 0:
                curr += int(a[i])
                i -= 1
            if j >= 0:
                curr += int(b[j])
                j -= 1 
            curr += carry 
            result.append(str(curr % 2))
            carry = curr // 2 
        return ''.join(reversed(result))

if __name__ == "__main__":
    a = "11"
    b = "1"
    # should be "100"
    print(Solution().addBinary(a, b))

    a = "1010"
    b = "1011"
    # should be "10101"
    print(Solution().addBinary(a, b))
