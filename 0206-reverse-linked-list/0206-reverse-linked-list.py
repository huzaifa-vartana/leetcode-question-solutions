# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next if head else None

        while curr:
            if prev == head:
                prev.next = None

            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


        return prev
        