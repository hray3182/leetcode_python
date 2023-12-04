from typing import List

# 問題描述：
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example :

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# 解題思路：
# 創建一個變數 common，賦值為列表中第一個字串
# 遍歷列表中的每一個字串，對比 common 和當前字串[:len(common)]
# 若是對比結果為 False，則將 common 長度 -1，直到對比結果為 True
# 若是切片長度為 0，則直接返回空字串

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common = strs[0]
        for i in range(1, len(strs)):
            while common != strs[i][:len(common)]:
                common = common[:-1]
                if common == "":
                    return ""
        return common

def main():
    strs = ["flower","flow","flight"]
    # should be "fl"
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

if __name__ == "__main__":
    main()
