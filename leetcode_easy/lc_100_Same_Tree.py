"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p = TreeNode(p)
        q = TreeNode(q)
        if (p.val == q.val): 
            if(p.left == q.left or p.right == q.right ):
                return True
            else:
                return False
            return False
        else:
            return False
        
s = Solution()
print(s.isSameTree([1,2,3],[1,2,3]))
#print(s.isSameTree([1,2],[1,null,2]))
print(s.isSameTree([1,2,1],[1,1,2])) 







