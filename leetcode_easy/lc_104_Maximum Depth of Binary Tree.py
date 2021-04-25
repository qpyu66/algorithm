"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


"""

# 40ms
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:  
        #root = TreeNode(root)
        #print(root)     
        if root == None:
            return 0
        else:
            la = self.maxDepth(root.right)
            lr = self.maxDepth(root.left)
        return max(la, lr) + 1


#code refactoring 28ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)


s = Solution()
print(s.maxDepth([3, 9, 20, None, None, 15, 7]))
#print(s.maxDepth([3, 9, 20, 10, None, 15, 7, None, None, None, None, None, None, None, 9]))
#print(s.maxDepth([1, None, 2]))
#print(s.maxDepth([]))     
