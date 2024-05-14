from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    if root is None:
        return []

    result = []
    queue = deque([root]) # Breadth-first-search algo, double extremité

    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

root1 = Node(Node(Node(None, None, 1), Node(None, None, 3), 8), Node(Node(None, None, 4), Node(None, None, 5), 9), 2)
print(tree_by_levels(root1))  

