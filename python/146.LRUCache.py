class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # mapping key to node
        self.dic = {}
        # head and tail with dummy node
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            self._remove(self.dic[key])
            self._add(self.dic[key])
            return self.dic[key].value
        else:
            return -1

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.dic:
            self._remove(self.dic[key])
        else:
            if len(self.dic) == self.capacity:
                p = self.head.next
                self._remove(p)
                del self.dic[p.key]
        node = self.Node(key, value)
        self._add(node)
        self.dic[key] = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        # add to tail
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

if __name__ == '__main__':
    sol = LRUCache(3)
