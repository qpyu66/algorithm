"""
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively? - see preTraverse_itr

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        root = TreeNode(root)
        if root is None:            
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)



     
    
s = Solution()
print(s.preorderTraversal([1,2,2,3]))
print(s.preorderTraversal([1]))    
print(s.preorderTraversal([]))                   
