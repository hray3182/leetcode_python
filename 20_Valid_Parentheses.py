# 通過測驗圖：https://imgur.com/IBkcZ5J

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# 解題思路：
# 宣告一個 hash table, Key 為右邊的括號，Value 為左邊的，以及一個 string stack
# 遍歷 s，若是當前的字元不在 hash table 中，則將當前字元放入 stack 中
# 若是當前字元在 hash table 中，則檢查 stack 最後一個字元是否為 hash table 中的 value
# 若是不是，則返回 False
# 若是，則將 stack 最後一個字元 pop 出來


class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c not in hash_table:
                stack.append(c)
            else:
                if stack and stack[-1] == hash_table[c]:
                    stack.pop()
                else:
                    return False
        return not stack

def main():
    s = "()[]{}"
    sol = Solution()
    print(sol.isValid(s))

if __name__ == "__main__":
    main()