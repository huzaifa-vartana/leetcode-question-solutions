# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head

        carry = 0
        while l1 or l2:

            curr_nodes_val = 0
            if l1:
                curr_nodes_val += l1.val
                l1 = l1.next
            if l2:
                curr_nodes_val += l2.val
                l2 = l2.next

            new_node_val = (carry + curr_nodes_val) % 10
            carry = (carry + curr_nodes_val) // 10
            ptr.val = new_node_val
            if (l1) or (l2):
                    ptr.next = ListNode(0)
                    ptr = ptr.next

        
        if carry > 0: ptr.next = ListNode(carry)

        return head








        