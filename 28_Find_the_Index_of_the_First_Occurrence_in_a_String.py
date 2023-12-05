# 通過圖：https://imgur.com/ApD0tM9

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# 解題思路：
# 直接循環比較

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle)+i] == needle:
                return i

        return -1   
        
if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "sad"
    # should be 0 
    print(Solution().strStr(haystack, needle))