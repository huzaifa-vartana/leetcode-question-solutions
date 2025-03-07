# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            new_val = curr.val * 2
            if new_val < 10:
                curr.val = new_val
            elif prev:
                curr.val = new_val % 10
                prev.val += 1
            elif prev is None:
                head = ListNode(1, curr)
                curr.val = new_val % 10

            prev = curr
            curr = curr.next
        
        return head