class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache:
    # Using a hashmap (as cache for O(1) retrieval and a linked list 
    # to easily move around least and most recurrent units)
    # Reference solution: https://youtu.be/7ABFKPK2hD4
    
    def __init__(self, capacity: int):
        self.cache = dict()  # cache of key -> node pointer.
        self.cap = capacity
        self.len = 0
        
        # initialize left (LRU) and right (MRU) pointers.
        self.left = Node(0, 0)  # Least recurrent used.
        self.right = Node(0, 0)  # Most recurrent used.
        self.left.next, self.right.prev = self.right, self.left
        
    # remove any node from the linked list
    def remove(self, node: Node):
        self.len -= 1
        
        p_node, n_node = node.prev, node.next
        p_node.next, n_node.prev = n_node, p_node
        
    
    # add a node at the right end.
    def insert(self, node: Node):
        self.len += 1
        
        prev_mru = self.right.prev
        prev_mru.next, node.next = node, self.right
        self.right.prev, node.prev = node, prev_mru
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # Also need to update this node as the most used.
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if key already present in cache, remove it since it'll be updated.
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key=key, val=value)
        self.insert(self.cache[key])
        
        if self.len > self.cap:
            # Exceed capacity, remove the lru
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)