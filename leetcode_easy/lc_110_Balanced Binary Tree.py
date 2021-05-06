"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

         if root is None:
            return True
        elif self.rootdepth(root) < 0:
            return False
        else:
            return True
            
    def rootdepth(self,r):
        if r is None:
            return 1
        ld = self.rootdepth(r.left)
        rd = self.rootdepth(r.right)
        lrd = ld-rd
        rld = rd-ld

        #음수일때
        if lrd < 0:
            lrd *= -1
        elif rld < 0:
            rld *= -1   

        if ld < 0 or rd < 0:
            return -1        
        elif lrd > 1 or rld >1:
            return -1       
        else:
            return max(ld,rd)+1

#
class Solution1(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return abs(self.depth(root.left) - self.depth(root.right)) <= 1
            else:
                return False

    def depth(self, root):
        if root is None:
            return -1
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1


s = Solution()
print(s.isBalanced([3,9,20,null,null,15,7]))   