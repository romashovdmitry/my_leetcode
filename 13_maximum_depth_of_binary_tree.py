from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

# Тест 1: дерево глубиной 3
# Tree: [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Ожидаемый результат: 3
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(Solution().maxDepth(root1))

# Тест 2: дерево из одного узла
# Tree: [1]
# Ожидаемый результат: 1
root2 = TreeNode(1)
print(Solution().maxDepth(root2))

# Тест 3: пустое дерево
# Tree: []
# Ожидаемый результат: 0
root3 = None
print(Solution().maxDepth(root3))


def print_queue(queue):
    """Распечатывает содержимое очереди в читаемом виде"""
    items = []
    for node, depth in queue:
        items.append(f"(val={node.val}, depth={depth})")
    print(f"Queue: [{', '.join(items)}]")


# Итеративное решение (BFS с обычным списком)
class SolutionIterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            print_queue(queue)
            node, depth = queue.pop(0)  # Берём первый элемент (как в очереди)
            max_depth = max(max_depth, depth)
            
            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth


print("\n--- Итеративное решение ---\n")
# Tree: [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(SolutionIterative().maxDepth(root1))
