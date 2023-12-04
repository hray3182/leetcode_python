from typing import List

# 測試通過圖：https://imgur.com/p9DOIL6

class Solution:
    # 解題思路：運用 hash table，將 target - 當前的數存到 map 中，K,V 為 target - 當前的數, 當前的 index
    # 循環時若是當前的數在 map 中，則代表當前的數與 map 中的數相加為 target，則返回 map 中的 index 與當前的 index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 創建一個hash table
        hash = {}
        # 用 enumerate 來遍歷 nums
        for i, num in enumerate(nums):
            if num not in hash:
                hash[target - num] = i
            else:
                return [hash[num], i]
        
        return []



def main():
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))

if __name__ == "__main__":
    main()
