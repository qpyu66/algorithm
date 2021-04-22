"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

"""

#36ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root == None:
            return True
        else:
            return self.mirror(root.right,root.left)
        
    def mirror(self,q,p):
        if (q is None and p is None):
            return True
        elif (q is None or p is None):
            return False
           
        if(q.val != p.val):
            return False
        else:
            return self.mirror(q.right,p.left) and self.mirror(q.left,p.right)
                

#code refactoring 16ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
        
#         return self.dfs(root, root)
        
#     def dfs(self, right, left):
        
#         if right == None and left == None:
#             return True
        
#         if right == None or left == None:
#             return False
        
#         return (left.val == right.val) and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)