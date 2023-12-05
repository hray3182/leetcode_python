# 通過圖：https://imgur.com/lEf3hEr

from typing import List

# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# 解題思路：
# Sorted, O(log n)，第一個想到的是二分查找

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1 
        while left <= right:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
            
        return left
            
if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    # should be 2
    print(Solution().searchInsert(nums, target))

    nums = [1,3,5,6]
    target = 2
    # should be 1
    print(Solution().searchInsert(nums, target))


            