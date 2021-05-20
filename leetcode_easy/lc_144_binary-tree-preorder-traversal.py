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
from typing import List
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


#code refactoring
#sample 20 ms submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        stack = [root]
        result = []
        
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result
     
    
s = Solution()
print(s.preorderTraversal([1,None,2,3]))
"""
[1] + null + 2
[2] + 3 + null
[3] + null + null
"""
print(s.preorderTraversal([1]))    
print(s.preorderTraversal([]))                   
