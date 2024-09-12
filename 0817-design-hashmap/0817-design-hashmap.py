class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        new_node = Node(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current.next:
            current = current.next
            print(current.val, end=' ')
        print()


class MyHashMap:

    def __init__(self):
        self.map = [LinkedList() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        current = self.map[index].head
        while current.next:
            current = current.next
            if current.val[0] == key:
                current.val[1] = value
                return
        self.map[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % 1000
        current = self.map[index].head
        while current.next:
            current = current.next
            if current.val[0] == key:
                return current.val[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        current = self.map[index].head
        while current.next:
            prev = current
            current = current.next
            if current.val[0] == key:
                prev.next = current.next
                return
