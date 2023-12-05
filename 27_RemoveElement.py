# 通過測試圖：https://imgur.com/LlBXiml

from typing import List

# https://leetcode.com/problems/remove-element/

# 給一個整數數列 list 及一個整數 i 作為輸入
# 若 list 中包含 i 將它移除

# 解題思路：
# 用快慢指針，將快指針的值賦給慢指針的當前 index
# 每當遇到需要移除的整數，慢指針就會比快指針少 1 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for quick, v in enumerate(nums):
            if v != val:
                nums[slow] = v
                slow += 1
        return slow

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print(Solution().removeElement(nums, val)) # 2
    print(nums) # [2,2,2,3]

    nums = [0,1,2,2,3,0,4,2]
    val = 0
    print(Solution().removeElement(nums, val)) # 5
    print(nums) # [0,1,3,0,4,0,4,2]