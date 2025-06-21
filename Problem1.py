"""
I built the LRU Cache using a hash map linking keys to nodes in a doubly linked list that tracks usage order, with the most recent near the head and least recent near the tail. To handle edge cases smoothly, I included dummy head and tail nodes. The addToHead method places nodes right after the head to mark them as recently used, while removeNode removes nodes from their current spots. This setup enables quick updates of node positions during cache operations.
Time Compelxity: O(1) for both the functions
Space Compelxity: O(1) since I am not using any auxilary space in these functions
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.hashMap = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addToHead(self, node):
        # function to add the node at the head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head
    
    def removeNode(self, node):
        # function to detach the node
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        
        # present in hashmap
        if key in self.hashMap:
            node = self.hashMap[key]
            self.removeNode(node)
            self.addToHead(node)
            return node.val
        # not present in hashmap
        return -1
        
    def put(self, key: int, value: int) -> None:

        # node is present
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            self.removeNode(node)
            self.addToHead(node)
        else:
            # node not present check capacity
            if len(self.hashMap) == self.capacity:
                prevNode = self.tail.prev
                self.removeNode(prevNode)
                del self.hashMap[prevNode.key]
            newNode = Node(key, value)
            self.addToHead(newNode)
            self.hashMap[newNode.key] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)