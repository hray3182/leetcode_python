# https://leetcode.com/problems/contains-duplicate/description/

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# create a hash map, add num in nums to the map, if any num exist, return true

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            if hash_map.get(num):
                return True
            hash_map[num] = 1
        return False
    
    
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums)) # False
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5]
    print(Solution().containsDuplicate(nums)) # False
    nums = [1, 1, 1, 1, 1]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 1, 1, 1, 2]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(Solution().containsDuplicate(nums)) # False
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
    print(Solution().containsDuplicate(nums)) # True
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6]

            