# 通過測試圖：https://imgur.com/tP9NqY7

from typing import List
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# 給一個升序排序整數列表，輸出不重覆數字的數量
# 解題思路：
# 設置一個變量記錄不重覆數字數量，也能當作index用
# 遇到不重覆的數字就放 list[不重覆數量 - 1] 的位置
# 遍歷檢查就行

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                j += 1
                nums[j-1] = nums[i]
        return j 


if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().removeDuplicates(nums)) # 2
    print(nums) # [1,2,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums)) # 5
    print(nums) # [0,1,2,3,4,2,2,3,4]