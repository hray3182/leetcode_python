from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        hash_map = {}
        sum = 0 

        while curr:
            sum += curr.val
            hash_map[sum] = curr
            curr = curr.next

        sum = 0
        curr = dummy

        while curr:
            sum += curr.val
            if sum in hash_map:
                curr.next = hash_map[sum].next
            curr = curr.next
        return  dummy.next

def build_linked_list(l):
    head = ListNode(l[0])
    curr = head
    for i in range(1, len(l)):
        curr.next = ListNode(l[i])
        curr = curr.next
    return head

def print_linked_list(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    l = [1, 2, 3, -3, -2]
    head = build_linked_list(l)
    print_linked_list(Solution().removeZeroSumSublists(head)) # [1]

    