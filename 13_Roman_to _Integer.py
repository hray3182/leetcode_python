# 通過測驗圖：https://imgur.com/X5K6Lm1

# 問題描述：將給定的羅馬數字（文字）轉換成數字

# 解題思路：用字典映射對應的數字，之後循環文字，
# 如果右邊的數字比左邊的數字大，則減去左邊的數字，反之則加上左邊的數字

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_table = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50,
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        result = 0
        for i, v in enumerate(s):
            if i < len(s) - 1 and hash_table[v] < hash_table[s[i + 1]]:
                result -= hash_table[v]
            else:
                result += hash_table[v]
        return result

def main():
    s = "MCMXCIV"
    sol = Solution()
    # should be 1994
    print(sol.romanToInt(s))

if __name__ == "__main__":
    main()
