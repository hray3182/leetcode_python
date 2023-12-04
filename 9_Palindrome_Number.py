# 通過測驗圖：https://imgur.com/eLGvx5G

# 問題描述：Given an integer x, return true if x is a palindrome, and false otherwise.
# 121 為 true, 123 為 false
# 限制： solve it without converting the integer to a string

# 解題思路：宣告一個變數 half，用運算式將x從個位數開始取出，並放入half中，直到x <= half
# 例如：x = 12321, half = 0
# 第一次：x = 1232, half = 1
# 第二次：x = 123, half = 12
# 第三次：x = 12, half = 123
# 此時迴圈結束，判斷 x == half or x == half // 10
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x = x // 10
        return x == half or x == half // 10
        
def main():
    x = 12321
    sol = Solution()
    print(sol.isPalindrome(x))

if __name__ == "__main__":
    main()