class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.key = data

class Tree:
    def __init__(self):
        self.root = None
        self.data = None
        self.Node = None

    def find(self, data):
        p = self.root
        while (p is not None) and (p.key != data):
            if data > p.key:
                p = p.right
            else:
                p = p.left
        return p

    def add(self, data):
        p = self.find(data)
        if p is not None:
            return
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        p = self.root
        while True:
            if data < p.key:
                if p.left is None:
                    p.left = node
                    node.parent = p
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    node.parent = p
                    break
                else:
                    p = p.right

    def print(self, root = 0):
        if root == 0:
            root = self.root
        if root is None:
            return
        if root.left is not None:
            self.print(root.left)
        print(root.data, end=" ")
        if root.right is not None:
            self.print(root.right)

    def leaves(self, node):
        if node is None:
            return
        else:
            if node.left is not None:
                self.leaves(node.left)
            if node.right is not None:
                self.leaves(node.right)
            if node.left is None and node.right is None:
                l.append(node.data)
        return l

tree = Tree()
l = []
s = list(map(int, input().split()))
for x in s:
    tree.add(x)
l = tree.leaves(tree.root)
print(*l)