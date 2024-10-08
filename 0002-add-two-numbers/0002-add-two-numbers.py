# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new_list_head = ListNode(0, None)
        itr = new_list_head

        while l1 or l2:
            sum_ = 0
            if l1:
                sum_ += l1.val 
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            
            sum_ += carry
            digit = sum_ % 10
            carry = sum_ // 10

            itr.val = digit
            if (l1) or (l2):
                itr.next = ListNode(0)
                itr = itr.next

        
        if carry > 0: itr.next = ListNode(carry)
        return new_list_head
