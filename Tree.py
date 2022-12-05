import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


def inOrderTraversal(root):
    if root is None:
        return None
    inorderTraversal(root.left)
    print(root.data)
    inorderTraversal(root.right)


def preOrderTraversal(root):
    if root is None:
        return None
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


def postOrderTraversal(root):
    if root is None:
        return None
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data)


def AdjDict(root):
    if root is None:
        return
    d[root.data] = []
    AdjDict(root.left)
    if root.left:
        d[root.data].append(root.left.data)
    if root.right:
        d[root.data].append(root.right.data)
    AdjDict(root.right)
    return d


def printAdjdict(aList):
    for i in aList:
        print(f'{i}:{d[i]}')


def BFS(al, root):
    if root is None:
        return
    queue = collections.deque([root.data])
    visited = []
    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    return visited


def DFS(al, root):
    if root is None:
        return
    stack = [root.data]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]

    return visited


def search(key, al, root):
    stack = [root.data]
    visited = []
    isFound = False
    while stack:
        node = stack.pop()
        if node == key:
            return True
        if node not in visited:
            visited.append(node)
            [stack.append(x) for x in al[node]]
    return isFound


if __name__ == '__main__':
    root = Node(0)
    root.insert(5)
    root.insert(4)
    root.insert(6)
    root.insert(2)
    root.insert(8)
    root.insert(10)
    root.insert(1)
    d = {}
    aList = AdjDict(root)
    print(BFS(aList, root))
    print(DFS(aList, root))
    # printAdjdict(aList)
