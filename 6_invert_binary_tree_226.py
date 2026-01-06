# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(
            self,
            root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        Solution().invertTree(root.left)
        Solution().invertTree(root.right)
        
        return root


t1_1 = TreeNode(4)

t2_1 = TreeNode(2)
t2_2 = TreeNode(7)

t3_1 = TreeNode(1)
t3_2 = TreeNode(3)
t3_3 = TreeNode(6)
t3_4 = TreeNode(9)

t1_1.left = t2_1
t1_1.right = t2_2

t2_1.left = t3_1
t2_2.right = t3_2

t2_1.left = t3_3
t2_2.right = t3_4


x = (Solution().invertTree(root=t1_1))

while x:
    print(f'rrot now -> {x.val}')
    x = x.left