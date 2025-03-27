class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            print("node", node.val, "prev", prev.val if prev else None, "head", head.val if head else None)
            nextt = node.next
            if node.val == val:
                if head == node:
                    head = nextt

                if prev: 
                    prev.next = nextt
                    
            else:
                prev = node

            node = nextt

        return head