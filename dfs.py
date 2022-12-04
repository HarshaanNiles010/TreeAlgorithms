class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.value) + ")"


def walk1(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)


def walk2(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)
