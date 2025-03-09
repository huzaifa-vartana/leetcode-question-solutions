class Node:
    def __init__(self, key = "X", val = "X", next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [Node() for _ in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        idx = key % 1000
        head = self.map[idx]

        while head:
            if head.key == key:
                head.val = value
                return None
            if not head.next:
                break
            head = head.next

        head.next = Node(key, value)

        return None


    def get(self, key: int) -> int:
        idx = key % 1000
        head = self.map[idx]
        while head:
            if head.key == key: return head.val
            head = head.next

        return -1
        

    def remove(self, key: int) -> None:
        idx = key % 1000
        head = self.map[idx]

        while head:
            if head and head.next and head.next.key == key:
                head.next = head.next.next
            head = head.next

        return None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)