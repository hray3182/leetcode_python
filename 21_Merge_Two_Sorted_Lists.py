# 通過測驗圖：https://imgur.com/DhBJHxh
from typing import Optional, List

# Problem description:
# https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.

# 解題思路：
# 1. 建立一個空鏈表
# 2. while 迴圈條件為某一個鏈的為 None
# 3. 比較兩個鏈表的值，將較小的值放入空鏈表中，並將該鏈表的 next 指向下一個鏈表
# 4. 若是其中一個鏈表為空，則將另一個鏈表的值全部放入空鏈表中

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        head = ListNode()
        cur = head

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        
        if list1 is None:
            cur.next = list2
        else:
            cur.next = list1
        return head.next

def main():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    # should be 1 -> 1 -> 2 -> 3 -> 4 -> 4
    sol = Solution()
    result = sol.mergeTwoLists(list1, list2)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()
