"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0
        elif (root.left is None and root.right is None):
            return 1

        # elif root.left is None:
        #     la = self.minDepth(root.right)
        #     lr = self.minDepth(root.left)
        #     return min(la, lr) + 1     
        # elif root.right is None:
        #     la = self.minDepth(root.right)
        #     lr = self.minDepth(root.left)
        #     return min(la, lr) + 1
        else:
            la = self.minDepth(root.right)
            lr = self.minDepth(root.left)
        return min(la, lr) + 1

        

    def createnode(self,x):
        node = TreeNode(x)
        for i in range(1,len(x)):      
            if i %2 == 1:
                node.left = x[i]
            else:
                node.right = x[i]
        return node

        

s = Solution()
print(s.minDepth([3,9,20,null,null,15,7]))
print(s.minDepth([2,null,3,null,4,null,5,null,6]))


