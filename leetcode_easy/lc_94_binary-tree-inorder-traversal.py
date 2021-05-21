"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:


Input: root = [1,2]
Output: [2,1]
Example 5:


Input: root = [1,null,2]
Output: [1,2]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left)+[root.val]  + self.inorderTraversal(root.right)
   

#code refactoring
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Soln1: Recursive (easy)

Soln2: Iterative
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        Stack = []
        ans = []
        node = root
        if not root: return []
        
        while (Stack or node):
            
            if node:
                Stack.append(node)
                node = node.left
            else:
                add_node = Stack.pop(-1)
                ans.append(add_node.val)
                
                node = add_node.right
        
        return ans
                
        
        '''
        
        def traverse(node):
            if not node: return
            
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        
        ans = []
        traverse(root)
        return ans
        '''



        
s = Solution()
print(s.preorderTraversal([1,None,2,3]))
print(s.preorderTraversal([1]))
print(s.preorderTraversal([1,2]))