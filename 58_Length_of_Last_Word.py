# pass https://imgur.com/undefined


# https://leetcode.com/problems/length-of-last-word/
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.


# 解題思路: 用 string.split 將字串分割後，回傳array最後一個item的長度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])

if __name__ == '__main__':
    solution = Solution()
    s = "Hello World   "
    print(solution.lengthOfLastWord(s))