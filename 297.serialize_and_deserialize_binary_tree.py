
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        q = collections.deque()
        q.append(root)
        s = []
        while q:
            node = q.popleft()
            if not node:
                s.append('n')
                s.append(',')
            else:
                s.append(str(node.val))
                s.append(',')
                q.append(node.left)
                q.append(node.right)
        return ''.join(s[:-1])


    def deserialize(self, data):
        s = data.split(',')
        N = len(s)
        if N < 2: return None
        root = TreeNode(int(s[0]))
        q = collections.deque()
        q.append(root)
        i = 1
        while i < N-1:
            p = q.popleft()
            if s[i] != 'n':
                p.left = TreeNode(int(s[i]))
                q.append(p.left)
            i+=1
            if s[i] != 'n':
                p.right = TreeNode(int(s[i]))
                q.append(p.right)
            i+=1
        return root

if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    s = codec.serialize(codec.deserialize('1,2,3,n,n,4,5,n,n,n,n'))
    print(s)

