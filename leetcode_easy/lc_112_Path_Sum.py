"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        root = TreeNode(root)
        slist = self.pasum(root, 0)
        for n in slist:
            if n == targetSum:
                return True   
            print("")
        return False       
    def pasum(self,root, nsum):
        #unsupported operand type(s) for +=: 'int' and 'list'
        if (root.left is None) and (root.right is None):
            nsum += root.val
            return nsum
        else:
            nsum = nsum+root.val
        return self.pasum(root.left, nsum) + self.pasum(root.right, nsum)


s = Solution()
#print(s.hasPathSum([5,4,8,11,13,4,7,2,1],22))
print(s.hasPathSum([1,2,3],5))






s = Solution()
print(s.hasPathSum([5,4,8,11,null,13,4,7,2,null,null,null,1],22))
#print(s.hasPathSum([1,2,3],5))
#print(s.hasPathSum([1,2],0))
